

```java
package com.vip8.pricemanage;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class SubtitleReader {

    public static Boolean isContainChinese(String text) {
        boolean containsChinese = text.matches(".*[\\u4E00-\\u9FA5].*");

        if (containsChinese) {
            // System.out.println("字符串包含中文字符");
            return true;
        } else {
            // System.out.println("字符串不包含中文字符");
            return false;
        }
    }

    public static Boolean isOnlyNumber(String text ) {
        boolean onlyDigits = text.matches("\\d+");

        if (onlyDigits) {
            // System.out.println("字符串只包含数字");
            return true;
        } else {
            // System.out.println("字符串包含其他字符");
            return false;
        }
    }
    public static Boolean isTimeLine(String text ) {
        boolean isTimeLine = text.matches("\\d+:\\d+:\\d+,\\d+ --> \\d+:\\d+:\\d+,\\d+");

        if (isTimeLine) {
            // System.out.println("字符串只包含数字");
            return true;
        } else {
            // System.out.println("字符串包含其他字符");
            return false;
        }
    }
    public static Boolean isMusicSentence(String text ) {
        if (text.contains("{") || text.contains("}")) {
            return true;
        }
        return false;
    }

    public static List<LocalTime> parseTimeRange(String timeRange) {
        Pattern pattern = Pattern.compile("(\\d{2}:\\d{2}:\\d{2},\\d{3}) --> (\\d{2}:\\d{2}:\\d{2},\\d{3})");
        Matcher matcher = pattern.matcher(timeRange);
        List<LocalTime> ranges = new ArrayList<>();

        if (matcher.matches()) {
            String startTimeStr = matcher.group(1);
            String endTimeStr = matcher.group(2);

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss,SSS");
            LocalTime startTime = LocalTime.parse(startTimeStr, formatter);
            LocalTime endTime = LocalTime.parse(endTimeStr, formatter);
            ranges.add(startTime);
            ranges.add(endTime);
        } else {
            System.out.println("时间范围格式不正确");
        }
        return ranges;
    }

    public static void sortByStrLength(List<String> sentences) {
        sentences.sort(new StringLengthComparator());
    }

    static class StringLengthComparator implements Comparator<String> {
        @Override
        public int compare(String str1, String str2) {
            return Integer.compare(str2.length(), str1.length());
        }
    }

    public static void sortByWordsNumber(List<String> sentences) {
        sentences.sort(new WordsNumberComparator());
    }

    public static String removePunctuation(String input) {
        // 使用正则表达式匹配英文标点符号
        String regex = "[\\p{Punct}&&[^']]";
        return input.replaceAll(regex, "");
    }

    public static Integer getSentenceWordsNumber(String sentence) {
        String result = removePunctuation(sentence);
        String[] strList1 = removePunctuation(result).split(" ");
        return strList1.length;
    }

    static class WordsNumberComparator implements Comparator<String> {
        @Override
        public int compare(String str1, String str2) {
            return Integer.compare(getSentenceWordsNumber(str2), getSentenceWordsNumber(str1));
        }
    }

    /**
     * 句子类型
     */
    @Getter
    @AllArgsConstructor
    static enum SentenceType {
        QUESTION(1,"疑问"),
        NORMAL(2,"肯定");
        private final Integer code;
        private final String desc;
    }

    public static List<String> filterBySentenceType(SentenceType type,List<String> sentences) {
        if (type.getCode().equals(SentenceType.NORMAL.getCode())) {
            return sentences.stream().filter(sentence -> !sentence.contains("?")).collect(Collectors.toList());
        } else if (type.getCode().equals(SentenceType.QUESTION.getCode())) {
            return sentences.stream().filter(sentence -> sentence.contains("?")).collect(Collectors.toList());
        }
        return new ArrayList<>();
    }



    public static void main(String[] args) {
        String filePath = "/Users/mozicong/codes/pricemanage/pricemanage-web/src/main/resources/Forrest.Gump.1994.REMASTERED.1080p.BluRay.X264-AMIABLE.英文.srt"; // 替换为你的字幕文件路径

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            StringBuilder sentence = new StringBuilder();
            StringBuilder timeLimeInfo = new StringBuilder();

            List<String> sentences = new ArrayList<>();
            List<String> timeLines = new ArrayList<>();


            while ((line = br.readLine()) != null) {
                if (isTimeLine(line)) {
                    if ("".contentEquals(timeLimeInfo)) {
                        timeLimeInfo.append(line);
                    }
                }
                if (!line.trim().isEmpty() && !isTimeLine(line) && !isContainChinese(line) && !isOnlyNumber(line)) {
                    sentence.append(line).append(" ");
                    if (line.matches(".*[.?!]")) {
                        // 打印数据
                        // System.out.println(timeLimeInfo.toString());
                        // System.out.println(sentence.toString());

                        sentences.add(sentence.toString().toLowerCase());
                        timeLines.add(timeLimeInfo.toString());
                        sentence = new StringBuilder(); // 清空句子缓存
                        timeLimeInfo = new StringBuilder();
                    }
                }
            }

            // 输出最后一个句子（如果有的话）
            if (sentence.length() > 0) {
                // System.out.println("last sentence is : " + sentence.toString());
                sentences.add(sentence.toString().toLowerCase());
            }

            // 输出时间线（如果有的话）
            if (timeLimeInfo.length() > 0) {
                // System.out.println("last sentence is : " + sentence.toString());
                timeLines.add(timeLimeInfo.toString());
            }

            // handleSentences
            System.out.println(" 句子的个数是: " + sentences.size() + "时间线数量是:" + timeLines.size());
            //sortByWordsNumber(sentences);
            //sentences.forEach(System.out::println);
            //filterBySentenceType(SentenceType.QUESTION,sentences).forEach(System.out::println);
            //filterBySentenceType(SentenceType.NORMAL,sentences).forEach(System.out::println);
            System.out.println("疑问句子的数量是: " + filterBySentenceType(SentenceType.QUESTION,sentences).size());
            System.out.println("肯定句子的数量是: " + filterBySentenceType(SentenceType.NORMAL,sentences).size());

            List<String> sentencesFilter = filterBySentenceType(SentenceType.QUESTION, sentences);
            sortByWordsNumber(sentencesFilter);
            sentencesFilter.forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```





```java
package com.vip8.pricemanage;

import org.bytedeco.ffmpeg.global.avcodec;
import org.bytedeco.ffmpeg.global.avutil;
import org.bytedeco.javacv.*;
import org.bytedeco.javacv.Frame;
import sun.font.FontDesignMetrics;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.Map;
import java.util.UUID;

/**
 * @author 李林奇
 * @apiNote 视频剪辑工具类
 * @version 1.0.0
 *
 * */
public class VideoUtil {

    public static String videoPath_temp_path= "/Users/mozicong/codes/pricemanage/pricemanage-web/src/main/resources/";

    /**
    *
    * @apiNote 切割视频指定的位置
    * @param videoPath 视频路径
    * @param start 视频开始时间 ，单位秒
    * @param end 视频结束时间
    * @param recodeAudio 是否录制音频
    * @return 生成文件路径
    * */

    public static String  cutVideo(String videoPath,Integer start,Integer end,boolean recodeAudio) throws FFmpegFrameGrabber.Exception, FFmpegFrameRecorder.Exception {
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(videoPath);
        grabber.start();
        String s = UUID.randomUUID().toString()+".mp4";
        FFmpegFrameRecorder fFmpegFrameRecorder = new FFmpegFrameRecorder(videoPath_temp_path + s,grabber.grabImage().imageWidth,grabber.grabImage().imageHeight,recodeAudio?1:0);
        fFmpegFrameRecorder.start();
        Frame frame = null;
        while ((frame=grabber.grabFrame(recodeAudio,true,true,false))!=null){
            if ((start==null?0:(start*1000000))<frame.timestamp&&(end == null || ((end * 1000000) > frame.timestamp))){
                fFmpegFrameRecorder.record(frame);
            }
        }

        fFmpegFrameRecorder.stop();
        fFmpegFrameRecorder.release();
        return s;
    }

    /**
     * @apiNote 视频添加水印
     * @param videoPath 视频路径
     * @param text 水印文本
     * @param x 水印位置x
     * @param y 水印位置y
     * @param color 水印颜色
     * @param fontSize 水印文字大小
     * @return 生成文件路径
     *
     * */
    public static String waterMark(String videoPath, String text, Integer x, Integer y, Color color, Integer fontSize) throws Exception {
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(videoPath);
        grabber.start();
        Frame frame = grabber.grabImage();

        String s = videoPath_temp_path + UUID.randomUUID().toString()+".mp4";
        FFmpegFrameRecorder recorder = new FFmpegFrameRecorder(s,frame.imageWidth,frame.imageHeight,0);
        recorder.start();
        int j= 0;
        while ((frame=grabber.grabImage())!=null){
            Java2DFrameConverter converter = new Java2DFrameConverter();
            BufferedImage bufImg = converter.getBufferedImage(frame);

            Font font = new Font("微软雅黑", Font.BOLD, 64);
//            String content = new SimpleDateFormat("yyyy-MM-dd").format(new Date());
//            String content1 = "字符滚动效果";
            FontDesignMetrics metrics = FontDesignMetrics.getMetrics(font);
            int width = bufImg.getWidth();//计算图片的宽
            int height = bufImg.getHeight();//计算高
            Graphics2D graphics = bufImg.createGraphics();
            graphics.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
            graphics.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER));
            graphics.drawImage(bufImg, 0, 0, bufImg.getWidth(), bufImg.getHeight(), null);

            graphics.setColor(color);
            graphics.setFont(new Font("微软雅黑", Font.BOLD, fontSize));
            graphics.drawString(text,  x, y);
            graphics.dispose();


            frame = converter.getFrame(bufImg);



            recorder.record(frame);
            j++;
        }
        grabber.stop();
        recorder.stop();
        recorder.release();
        return s;
    }

    /**
    * @apiNote 合并音视频
    * @param audioPath 音频路径
    * @param videoPath 视频路径
    * @return 最终生成文件地址
    *
    * */

    public String mergeAV(String audioPath,String videoPath){
        String outputPath = videoPath_temp_path+UUID.randomUUID()+".mp4";
        try (FFmpegFrameGrabber imageGrabber = new FFmpegFrameGrabber(videoPath);
             FFmpegFrameGrabber audioGrabber = new FFmpegFrameGrabber(audioPath)) {
            imageGrabber.start();
            audioGrabber.start();
            try (FFmpegFrameRecorder recorder = new FFmpegFrameRecorder(outputPath, imageGrabber.getImageWidth(), imageGrabber.getImageHeight(),
                    1);) {

                recorder.setInterleaved(true);
                recorder.setVideoCodec(avcodec.AV_CODEC_ID_H264);
                recorder.setFormat("mp4");
                recorder.setPixelFormat(avutil.AV_PIX_FMT_YUV420P); // yuv420p
                int frameRate = 25;
                recorder.setFrameRate(frameRate);
                recorder.setGopSize(frameRate * 2);
                recorder.setAudioOption("crf", "0");
                recorder.setAudioQuality(0);// 最高质量
                recorder.setAudioCodec(avcodec.AV_CODEC_ID_AAC);
                recorder.setAudioChannels(2);
                recorder.setSampleRate(44100);
                recorder.start();
                long videoTime = imageGrabber.getLengthInTime();
                Frame imageFrame = null;
                while ((imageFrame = imageGrabber.grabImage()) != null) {
                    recorder.record(imageFrame);
                }
                long audioPlayTime = 0L;
                Frame sampleFrame = null;
                while ((sampleFrame = audioGrabber.grabSamples()) != null || audioPlayTime < videoTime) {
                    if (sampleFrame == null) {
                        audioGrabber.restart();//重新开始
                        sampleFrame = audioGrabber.grabSamples();
                        videoTime -= audioPlayTime;
                    }
                    recorder.record(sampleFrame);
                    audioPlayTime = audioGrabber.getTimestamp();
                    if (audioPlayTime >= videoTime) {
                        break;
                    }
                }
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return outputPath;

    }


    /**
     *
    * @apiNote 合并多个视频
     * @param list 要合并的视频列表
     * @param outputPath 输出文件位置
     * @return 返回输出文件位置
     *
     *
    * */
    public static String mergeVideo(java.util.List<String> list,String outputPath) throws FrameGrabber.Exception {

        ArrayList<FFmpegFrameGrabber> grabbers = new ArrayList<>();
        OpenCVFrameGrabber grabber1 = new OpenCVFrameGrabber(list.get(0));

        grabber1.start();
        Frame frame1 = grabber1.grabFrame();
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
            grabbers.add(new FFmpegFrameGrabber(list.get(i)));
            FFmpegFrameGrabber grabber = grabbers.get(i);
            grabber.start();
        }
        Map<String, String> metadata = grabbers.get(0).getMetadata();
        FFmpegFrameRecorder fFmpegFrameRecorder = new FFmpegFrameRecorder(outputPath+"temp0"+".mp4",frame1.imageWidth,frame1.imageHeight,grabbers.get(0).getAudioChannels());
        grabber1.stop();
        fFmpegFrameRecorder.setFormat("mp4");
        fFmpegFrameRecorder.setAudioChannels(2);
        fFmpegFrameRecorder.setGopSize(4);
        try {
            fFmpegFrameRecorder.start();
            for (int i = 0; i < grabbers.size(); i++) {
                FFmpegFrameGrabber grabber = grabbers.get(i);
                if (i>0){

                    FFmpegFrameGrabber grabber2 = new FFmpegFrameGrabber(outputPath + "temp" + (i - 1) + ".mp4");
                    grabber2.start();
                    fFmpegFrameRecorder = new FFmpegFrameRecorder(outputPath+"temp"+(i)+".mp4",frame1.imageWidth,frame1.imageHeight,grabber2.getAudioChannels());
                    fFmpegFrameRecorder.start();
                    grabber2.setFormat("mp4");
                    System.out.println(grabber2.getFormat());
                    Frame avFrame = null;
                    while ((avFrame = grabber2.grabFrame())!=null){
                        fFmpegFrameRecorder.record(avFrame);
                    }
                    grabber2.release();
                    grabber2.stop();
                    grabber2.close();
                    new File(outputPath + "_temp_" + (i - 1) + ".mp4").deleteOnExit();
                }

                Frame avFrame = null;
                while ((avFrame = grabber.grabFrame(true,true,true,false))!=null){
//                    fFmpegFrameRecorder.record(avFrame);
                    fFmpegFrameRecorder.record(avFrame);
                }
                grabber.stop();
                fFmpegFrameRecorder.stop();
                System.gc();
            }
            fFmpegFrameRecorder.stop();
            File file = new File(outputPath + "temp" + (grabbers.size() - 1) + ".mp4");
            file.renameTo(new File(outputPath+".mp4"));
            return outputPath;
        } catch (FFmpegFrameRecorder.Exception | FrameGrabber.Exception e) {
            e.printStackTrace();
            try {
                fFmpegFrameRecorder.stop();
                for (int i = 0; i < grabbers.size(); i++) {
                    grabbers.get(i).stop();
                }
            } catch (FFmpegFrameRecorder.Exception | FrameGrabber.Exception ex) {
                ex.printStackTrace();
            }
           throw new RuntimeException("合成失败");
        }

    }

}

```



```java
        <dependency>
            <groupId>org.bytedeco</groupId>
            <artifactId>javacv-platform</artifactId>
            <version>1.5.6</version> <!-- 根据最新版本更新 -->
        </dependency>
```



```python
from itertools import groupby

import requests
from lxml import etree
import pymysql


def insertDataTODb(data: []):
    global conn
    try:
        # 1. 创建连接（Connection）
        conn = pymysql.connect(host='192.168.88.88', port=3306,
                               user='root', password='demo',
                               database='english', charset='utf8mb4',
                               autocommit=True)
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            for word in data:
                sql = "insert into words_outside (english ,cx,level) values ('%s','%s','%s');" \
                      % (word["english"], word["cx"], word["level"],)
                affected_rows = cursor.execute(sql)
                if affected_rows == 1:
                    print('添加数据成功')
    finally:
        # 5. 关闭连接释放资源
        conn.close()


# 根据词性分组
def groupByField(data: [], f):
    data_sort = sorted(data, key=lambda x: x[f])
    data_group = groupby(data_sort, key=lambda x: x[f])
    for key, group in data_group:
        print(key, len(list(group)))
    return data_group


if __name__ == '__main__':
    resp = requests.get(
        url='https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000',
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
        # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
        # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    )

    htmlInfo = resp.text
    htmlObject = etree.HTML(htmlInfo)
    wordsInfos = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/a')
    wordsCXs = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/span')
    wordsLevels = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/div/span')
    words = []
    for english, cx, level in zip(wordsInfos, wordsCXs, wordsLevels):
        if level.text != 'c1':
            words.append({
                "english": english.text,
                "cx": cx.text,
                "level": level.text
            })
    print(len(words))
    # insertDataTODb(words)
    data_group = groupByField(words, "cx")
    data_group = groupByField(words, "level")

```



```python
import json
from itertools import groupby

import requests
from lxml import etree
import pymysql


def insertDataTODb(data: []):
    global conn
    try:
        # 1. 创建连接（Connection）
        conn = pymysql.connect(host='192.168.88.88', port=3306,
                               user='root', password='demo',
                               database='english', charset='utf8mb4',
                               autocommit=True)
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            for word in data:
                sql = "insert into words_outside (english ,cx,level) values ('%s','%s','%s');" \
                      % (word["english"], word["cx"], word["level"],)
                affected_rows = cursor.execute(sql)
                if affected_rows == 1:
                    print('添加数据成功')
    finally:
        # 5. 关闭连接释放资源
        conn.close()


# 根据词性分组
def groupByField(data: [], f, isPrint):
    data_sort = sorted(data, key=lambda x: x[f])
    result_group = groupby(data_sort, key=lambda x: x[f])
    result = {}
    var1 = []
    for key, group in result_group:
        result[key] = list(group)
        var1.append({"key": key, "value": len(result[key])})
    var1 = sorted(var1, key=lambda x: x["value"], reverse=True)
    for var in var1:
        if isPrint:
            print(var['key'], var['value'])
    return result


def exportWords(level1, cx1, ls):
    filename = str(level1 + "_" + cx1 + "_" + str(len(list(ls))) + ".txt")
    f = open(filename, 'w')
    for cc in list(ls):
        f.write(str(cc["english"]) + "\n")
    f.close()


def doExportByLevel(k1, rss):
    noun = []
    verb = []
    adjective = []
    adverb = []
    other = []
    for k2, v2 in rss.items():
        if k2 == "noun":
            for n in list(v2):
                noun.append(n)
        elif k2 == "verb":
            for n in list(v2):
                verb.append(n)
        elif k2 == "adjective":
            for n in list(v2):
                adjective.append(n)
        elif k2 == "adverb":
            for n in list(v2):
                adverb.append(n)
        else:
            for n in list(v2):
                other.append(n)
    # 导出
    exportWords(k1, "noun", noun)
    exportWords(k1, "verb", verb)
    exportWords(k1, "adjective", adjective)
    exportWords(k1, "adverb", adverb)
    exportWords(k1, "other", other)


def groupByTowField(ws: [], key1, key2):
    rs = groupByField(ws, key1, False)
    for k1, v1 in rs.items():
        print(f"=================>", k1, len(list(v1)))
        rss = groupByField(list(v1), key2, True)
        doExportByLevel(k1, rss)


if __name__ == '__main__':
    resp = requests.get(
        url='https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000',
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
        # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
        # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    )

    htmlInfo = resp.text
    htmlObject = etree.HTML(htmlInfo)
    wordsInfos = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/a')
    wordsCXs = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/span')
    wordsLevels = htmlObject.xpath('//*[@id="wordlistsContentPanel"]/ul/li/div/span')
    words = []
    for english, cx, level in zip(wordsInfos, wordsCXs, wordsLevels):
        if level.text != 'c1' and level.text != 'b2':
            words.append({
                "english": english.text,
                "cx": cx.text,
                "level": level.text
            })
    print(len(words))
    # insertDataTODb(words)
    groupByTowField(words, "level", "cx")
    # groupByTowField(words, "cx", "level")

# noun 1479 名词
# verb 609 动词
# adjective 523 形容词
# adverb 186 副词
# pronoun 41 代词
# preposition 38 介词
# determiner 26 限定词
# conjunction 19 连词
# number 16 数词
# exclamation 13 感叹词
# modal verb 8 情态动词
# ordinal number 5 序数词
# auxiliary verb 2 助动词
# definite article 1 定冠词
# indefinite article 1 不定冠词
# infinitive marker 1 不定式

```





[a1_adjective_191.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479076-9f835e2a-805f-4a72-9433-94572fa22721.txt)

[a1_adverb_75.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479293-4c42fda9-e23a-4043-8c0d-ce9287d95d55.txt)

[a1_noun_528.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479373-aef3e738-2a58-4128-9f5c-fce212ead7a8.txt)

[a1_other_82.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479473-d329f95f-b40f-408c-a7a0-d6b95f35162a.txt)

[a1_verb_200.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479579-010b30f3-fd19-499a-a4c7-2a612f936002.txt)



[a2_adjective_178.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479671-e71f20b1-0130-4af5-a250-88b03715ec60.txt)

[a2_adverb_66.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479796-5a6b9d44-d245-440c-8420-902768ee2df9.txt)

[a2_noun_489.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479863-4cb363a2-e8b3-4006-9464-8a5384c68755.txt)

[a2_other_49.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921479947-e9ab6aba-7c6a-41ff-bf0a-6df53117ab32.txt)

[a2_verb_208.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480027-2e3e475a-cecd-43de-9e38-472fb045e0d2.txt)



[b1_adjective_154.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480120-d2c5fa95-00a4-423b-9cc5-d33cd997490c.txt)

[b1_adverb_45.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480218-08b87751-5308-4157-8e89-cf1fb363ff55.txt)

[b1_noun_462.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480304-f092e1fa-d136-4a16-b272-c0cd2b826026.txt)

[b1_other_40.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480423-7bb7a402-965a-49f4-a53d-4740a42eac44.txt)

[b1_verb_201.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480505-d5db34b8-bb2c-4101-90c9-9b6a41ea86ca.txt)



[b2_adjective_296.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480588-a978fde6-b82d-46f3-9067-5b97efccbfeb.txt)

[b2_adverb_105.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480720-fd323071-e1cf-4647-bd77-e87bb95340ea.txt)

[b2_noun_786.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480844-d4299f3e-8052-4aa5-9f47-9eebd95d5b14.txt)

[b2_other_65.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921480941-7d13b2f4-507c-495c-9dc0-4264bd73a592.txt)

[b2_verb_319.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481103-b66bb6f0-2788-4d98-b5f6-b81c9ca193f1.txt)



[c1_adjective_257.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481221-503a7cf7-e714-4271-90cf-84be02b0f005.txt)

[c1_adverb_76.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481367-bc675988-b379-44e6-84ad-14cf2f5ebc21.txt)

[c1_noun_695.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481471-85f4fe95-634e-4f02-a9ee-c3cbe7ddc3c0.txt)

[c1_other_57.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481670-61f1a053-5d1e-4c2e-9a01-5fd245c8ad5e.txt)

[c1_verb_319.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481751-dcac9b14-bb5d-4682-b7a3-76b95121a742.txt)





<details class="lake-collapse"><summary id="udadd6ddf"><span class="ne-text">content</span></summary><p id="u99648a1a" class="ne-p"><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921481875-17692f12-3434-4ffc-8785-9f11f6013346.txt" id="uaaf28565" class="ne-card-file">📎a1_adjective_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482094-c8b8db02-18b0-4cbb-9f74-9e3eb0f45365.txt" id="u2d140381" class="ne-card-file">📎a1_adjective_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482171-ea741b0a-69f2-48d6-b7b0-f2dc82b8e5dc.txt" id="uc2e45813" class="ne-card-file">📎a1_adjective_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482256-ac278b5a-a6c8-4b78-8913-591a1d0b01cb.txt" id="uba70e1a1" class="ne-card-file">📎a1_adjective_chapter4_41.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482352-43f6e151-267e-4eb3-b96b-d10e5d040996.txt" id="u3e157b73" class="ne-card-file">📎a1_adverb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482422-b5b74fcb-8082-4370-a204-070f844c91bd.txt" id="u3fef65b1" class="ne-card-file">📎a1_adverb_chapter2_25.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482512-b269cc9e-6b96-4ad2-9839-1f385b941490.txt" id="uccf591ba" class="ne-card-file">📎a1_noun_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482613-372e0bb2-bc0c-48ce-9fa3-df62019e1ce4.txt" id="u78cebba7" class="ne-card-file">📎a1_noun_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482687-321153ad-c0cd-4914-a2dd-6b4621755525.txt" id="u9852abb1" class="ne-card-file">📎a1_noun_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482751-d6e1af24-8402-4717-ba17-933ec6c4df8d.txt" id="u15d5e260" class="ne-card-file">📎a1_noun_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921482833-110d0ba5-097a-4346-8c2f-07def12d79b5.txt" id="u9ac1a1d7" class="ne-card-file">📎a1_noun_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483010-a74b9262-516e-4add-8731-a0fcf45c8145.txt" id="u4aec7426" class="ne-card-file">📎a1_noun_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483082-a69adefa-d7ff-4d7d-bdea-be7cee7c8da0.txt" id="uff3826e8" class="ne-card-file">📎a1_noun_chapter7_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483179-faab9539-a4ff-4a16-b4d6-c42d4fd0ad39.txt" id="u2ba72cba" class="ne-card-file">📎a1_noun_chapter8_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483283-b933ff6a-5eaa-4a10-85ec-8aea48d1bf62.txt" id="u51608b92" class="ne-card-file">📎a1_noun_chapter9_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483469-9db5bc9a-a0c1-435b-a5e5-a16755f8bf48.txt" id="u5e6e249b" class="ne-card-file">📎a1_noun_chapter10_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483595-9ada4fc5-e68c-4adb-b9bc-15a9a822cdba.txt" id="u13fa2764" class="ne-card-file">📎a1_noun_chapter11_28.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483657-976f050a-e643-4b11-b120-5fbfba3ff4c0.txt" id="u2e2f513c" class="ne-card-file">📎a1_other_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483737-51592f14-d938-41fc-be66-8822f9b1e5ff.txt" id="uf4a44340" class="ne-card-file">📎a1_other_chapter2_32.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483813-69d0820f-79d3-48ca-ab1f-3480ce9bca02.txt" id="u1cee3113" class="ne-card-file">📎a1_verb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483903-2b5c2cf2-a2e5-45fd-aa47-640c32ff1cf2.txt" id="ua05486c5" class="ne-card-file">📎a1_verb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921483975-47ee4f33-0eed-4441-88f6-e39e590361c3.txt" id="u80f59683" class="ne-card-file">📎a1_verb_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484065-3e7dccf6-bf35-4575-a8ae-25fca3835321.txt" id="u795f2c58" class="ne-card-file">📎a1_verb_chapter4_50.txt</a></p><p id="uccf5f662" class="ne-p"><br></p><p id="ua9e6ccf9" class="ne-p"><br></p><p id="u64b05a98" class="ne-p"><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484126-daf5f51b-5856-431f-bd8a-9a2ea63fcee5.txt" id="uf37e8ab7" class="ne-card-file">📎a2_adjective_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484194-13273b3e-cdf5-4734-9d07-aaa5aafd1711.txt" id="u2c6cb50d" class="ne-card-file">📎a2_adjective_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484272-2ad58cc8-fa97-43fc-9f97-767bf4b141e9.txt" id="u795e3140" class="ne-card-file">📎a2_adjective_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484342-9eebd9db-61dd-4e5b-a579-9aca90f36b6a.txt" id="u72b9bd79" class="ne-card-file">📎a2_adjective_chapter4_28.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484411-a352ba9c-956f-43d6-998e-a61a95a456a6.txt" id="u08832c61" class="ne-card-file">📎a2_adverb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484513-31a3230e-a647-46da-b70c-1c60202a0f4e.txt" id="u14869fbb" class="ne-card-file">📎a2_adverb_chapter2_16.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484595-067fb543-f9b8-4334-bdb2-f9ded8500ff8.txt" id="uf42ceb20" class="ne-card-file">📎a2_noun_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484672-3901f571-0ab1-4816-b3ba-ac66c3ef1506.txt" id="uae0a5a45" class="ne-card-file">📎a2_noun_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484805-f733994b-a751-403a-b923-437ed71c79cc.txt" id="u9b65e9c8" class="ne-card-file">📎a2_noun_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484893-08f14a84-a8d5-4dcd-a674-401317e5713a.txt" id="u8c734923" class="ne-card-file">📎a2_noun_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921484965-72243280-4f58-497e-8b4f-57472418895b.txt" id="u64726753" class="ne-card-file">📎a2_noun_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485059-15b3d012-6b95-4e9e-b298-63d926fe2529.txt" id="uaa89ce23" class="ne-card-file">📎a2_noun_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485140-9327eec1-5267-4e01-8f90-e8b5cfd83aab.txt" id="u2bdc8541" class="ne-card-file">📎a2_noun_chapter7_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485212-cf609426-1c06-4fcb-af31-fb1eeeea11e2.txt" id="uc721126c" class="ne-card-file">📎a2_noun_chapter8_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485280-e32d3c09-ee08-4a01-be8b-23e7aa3c0346.txt" id="ua3513ffd" class="ne-card-file">📎a2_noun_chapter9_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485370-78ea76f7-00ea-4498-99c0-740f9d81bd5f.txt" id="u14435166" class="ne-card-file">📎a2_noun_chapter10_39.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485421-64dd53f3-cc0e-4b9d-b416-9dd55d39fefe.txt" id="u2a8a509b" class="ne-card-file">📎a2_other_chapter1_49.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485509-d308d27d-c836-4a0c-9738-34de35eb6350.txt" id="ubb43a5ed" class="ne-card-file">📎a2_verb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485568-672fa16b-6140-4d3d-94ff-608053628383.txt" id="u07fe26d0" class="ne-card-file">📎a2_verb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485643-f6f4a434-4700-42d8-89f7-e5be9f20c7c6.txt" id="u64ca7b3f" class="ne-card-file">📎a2_verb_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485718-09f5e227-8e7d-4d3f-a22e-af0c75e09ff8.txt" id="ud46cc0e6" class="ne-card-file">📎a2_verb_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485781-48dc65a8-759e-47e8-be5c-9c7abacff4d4.txt" id="u3c7ed213" class="ne-card-file">📎a2_verb_chapter5_8.txt</a></p><p id="u8e6a98bb" class="ne-p"><br></p><p id="u20435f4e" class="ne-p"><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485844-571633dc-92fb-44a4-95e7-e8383e9cb552.txt" id="u293c2977" class="ne-card-file">📎b1_adjective_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921485930-3c4fd1e3-6cbf-4906-91d4-d86d4dc65588.txt" id="ubbf17fb0" class="ne-card-file">📎b1_adjective_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486045-3d78a60d-64be-41d6-9797-f51b74260eca.txt" id="uba43c1cf" class="ne-card-file">📎b1_adjective_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486151-49e0cc77-22c6-4fe3-a10c-d1d642626c15.txt" id="u8b5974bc" class="ne-card-file">📎b1_adjective_chapter4_4.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486213-5ecc4d13-08bd-431a-8397-4da8a51f21a4.txt" id="udee7d6ce" class="ne-card-file">📎b1_adverb_chapter1_45.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486286-8e3c31ae-4a28-415f-bcb7-70f20a827cca.txt" id="u92d62f3d" class="ne-card-file">📎b1_noun_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486357-bdaccd7d-37e8-4f0e-9729-568cd257ce1b.txt" id="u942504f3" class="ne-card-file">📎b1_noun_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486464-22418dfe-648d-49c7-9568-32cf1f6dacc1.txt" id="ue2e72dcb" class="ne-card-file">📎b1_noun_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486543-39588db3-cf44-4ee1-8409-9435eb653229.txt" id="u545fb287" class="ne-card-file">📎b1_noun_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486650-9f0c6973-0acc-4e4b-b784-229a008b8153.txt" id="u5cd44a80" class="ne-card-file">📎b1_noun_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486710-ffede075-fea1-4ba6-b67d-d2c3b080db63.txt" id="u1239fa81" class="ne-card-file">📎b1_noun_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486767-b6b064ec-b645-4674-8e5a-aa2c763d3f18.txt" id="u111555a0" class="ne-card-file">📎b1_noun_chapter7_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486844-5817fc29-2eef-44e0-8171-f4f6864e50f4.txt" id="u923053b2" class="ne-card-file">📎b1_noun_chapter8_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921486938-97131c9e-43fa-4f83-af91-b67ae58d698e.txt" id="udc907a74" class="ne-card-file">📎b1_noun_chapter9_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487011-6e3f185b-aa84-458c-a300-ec8b381aa5f1.txt" id="u8c7b2216" class="ne-card-file">📎b1_noun_chapter10_12.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487132-75d1b062-f88b-42c2-a9cc-27f47bc3cac2.txt" id="u1eac3637" class="ne-card-file">📎b1_other_chapter1_40.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487239-f55d1f08-88ad-4caa-9609-7c2568be6a12.txt" id="u2db02049" class="ne-card-file">📎b1_verb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487338-c7a97b27-7ef3-4368-b19f-9ec14c43a78f.txt" id="u1b8a2056" class="ne-card-file">📎b1_verb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487429-a95824f8-c670-4eaa-aff7-c8319aef92c2.txt" id="u9171b8ff" class="ne-card-file">📎b1_verb_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487502-ffa30996-965e-499f-9f23-f1196ef28583.txt" id="uf4682e71" class="ne-card-file">📎b1_verb_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487576-5ae2e79d-10f2-41c7-851d-790da5d2a4f8.txt" id="u377521c4" class="ne-card-file">📎b1_verb_chapter5_1.txt</a></p><p id="udb11b041" class="ne-p"><br></p><p id="ub58ef383" class="ne-p"><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487662-ba668a6c-3902-4dd2-883a-7264acacbd6e.txt" id="ueafd4175" class="ne-card-file">📎b2_adjective_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487873-95761427-fd48-4517-8618-e88b0dd07ef0.txt" id="u5d2d100a" class="ne-card-file">📎b2_adjective_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921487970-23a2a88f-2eb7-4c57-a10e-cfdd1327e8b3.txt" id="u61ff33f4" class="ne-card-file">📎b2_adjective_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488047-d1063227-8168-4074-9e79-665a21b967b6.txt" id="u608e0470" class="ne-card-file">📎b2_adjective_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488157-21c74e6b-b0d7-4397-9815-22f3472c1ea8.txt" id="u37fa78b7" class="ne-card-file">📎b2_adjective_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488275-7ffd1cdb-5e37-4c52-b6f8-b4ae8e6eb045.txt" id="ud73efe77" class="ne-card-file">📎b2_adjective_chapter6_46.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488338-12656c18-dc82-4759-8d4d-7ffcea0280e8.txt" id="uc21c9adf" class="ne-card-file">📎b2_adverb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488437-acd0aa54-b05b-4d3e-b0b8-6f41c0ad79d0.txt" id="u2a0704fd" class="ne-card-file">📎b2_adverb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488530-d6f451a0-9c34-44d9-814d-b804776cebb0.txt" id="u0cf7fd5a" class="ne-card-file">📎b2_adverb_chapter3_5.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488646-f33d232f-c2a4-4b9d-b221-e8e60c659397.txt" id="u4cd11fb8" class="ne-card-file">📎b2_noun_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488764-08e34827-29fb-46e7-9773-62e16e30eb7b.txt" id="ue65ff48d" class="ne-card-file">📎b2_noun_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488879-c4cd70b2-3896-46a0-8bc1-90581b0323f1.txt" id="udd0f11f9" class="ne-card-file">📎b2_noun_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921488953-e5927bdc-6408-4481-9855-7988d343ac26.txt" id="ufad94375" class="ne-card-file">📎b2_noun_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489031-376754d2-346e-4571-a4cd-37ae91892634.txt" id="u4425df6e" class="ne-card-file">📎b2_noun_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489100-ae2c3aab-5638-44ba-9cc4-853f9756f236.txt" id="u317aae63" class="ne-card-file">📎b2_noun_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489207-3d60ee31-06aa-48ed-a99e-7c4393d92fb2.txt" id="ucaa591b4" class="ne-card-file">📎b2_noun_chapter7_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489312-99c680c3-030c-4b87-af93-14b1f43f3780.txt" id="uf9d01496" class="ne-card-file">📎b2_noun_chapter8_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489378-64f47de6-71b0-4fd0-85ec-5d3dd76922fc.txt" id="uf0d318e4" class="ne-card-file">📎b2_noun_chapter9_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489479-7eabde4a-41c9-4ddb-a488-141e93a2bf1e.txt" id="u9c2a15a0" class="ne-card-file">📎b2_noun_chapter10_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489552-90a14f99-a2b2-440a-b3eb-084d6872ef48.txt" id="uc12f3bf0" class="ne-card-file">📎b2_noun_chapter11_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489629-6d0d2c3e-c5dc-437f-a421-7fa7e9b0b68c.txt" id="ue6e882d0" class="ne-card-file">📎b2_noun_chapter12_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489703-447840a4-b2a7-4940-97b3-67467f962721.txt" id="u339503ac" class="ne-card-file">📎b2_noun_chapter13_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489780-9d8ca2c8-6921-49ec-a9e6-f3dc525629ec.txt" id="ua92ddcd4" class="ne-card-file">📎b2_noun_chapter14_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489844-bb920f47-9527-4294-bf0f-affc932c5594.txt" id="ue4bb3fbf" class="ne-card-file">📎b2_noun_chapter15_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921489942-af3b3f97-49c4-4f30-9ee4-cc3ee024892b.txt" id="u3dd250dc" class="ne-card-file">📎b2_noun_chapter16_36.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490034-178bf580-eeba-4886-952b-5f026ca483ae.txt" id="u6929d417" class="ne-card-file">📎b2_other_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490099-4d7de2e5-cbf1-4761-834c-30dc215581ef.txt" id="u6a764797" class="ne-card-file">📎b2_other_chapter2_15.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490199-064218c7-49f2-4d26-9d49-32a26fbc38df.txt" id="u1ef23310" class="ne-card-file">📎b2_verb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490280-e99f6af9-090d-4123-ba08-619d8c970dc6.txt" id="uce5e40d5" class="ne-card-file">📎b2_verb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490371-a7949226-b867-40ea-90d1-1c4fb00dbf35.txt" id="u9abb1d5f" class="ne-card-file">📎b2_verb_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490441-52b4cf55-c2c3-415f-99be-4b00558c5073.txt" id="u2dad96e4" class="ne-card-file">📎b2_verb_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490560-1661d576-daa7-4d31-89bc-2fc46b76cf01.txt" id="u575a880d" class="ne-card-file">📎b2_verb_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490750-bcd17e2a-9226-49d7-af7c-bcd06c8fad6e.txt" id="u937ae2a5" class="ne-card-file">📎b2_verb_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490830-c7552c05-7d71-4b05-9dce-308694465baa.txt" id="u761742dd" class="ne-card-file">📎b2_verb_chapter7_19.txt</a></p><p id="uf1786d0a" class="ne-p"><br></p><p id="udb6904f6" class="ne-p"><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921490999-fd682fab-40ab-4617-bc8d-b7fcce819e1f.txt" id="u907acdc1" class="ne-card-file">📎c1_adjective_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491072-1f93d6e3-6f2d-4b0e-9f72-8aad6c6c6cbb.txt" id="uea89e78a" class="ne-card-file">📎c1_adjective_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491165-e7d9ee10-2f64-443f-a522-7c70d3e6f5a9.txt" id="ud782dacc" class="ne-card-file">📎c1_adjective_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491229-5e88958a-1ba0-408c-a7d4-bb1d4bb87cb3.txt" id="u769d0189" class="ne-card-file">📎c1_adjective_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491342-fc420489-942d-4df6-9506-3620e0da9108.txt" id="u08b9a223" class="ne-card-file">📎c1_adjective_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491439-13eafb00-0628-45b5-8e92-26a53824171a.txt" id="uf7fed780" class="ne-card-file">📎c1_adjective_chapter6_7.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491518-f64a30fb-b2b0-4c85-bd38-4ea924f79287.txt" id="ufb6603fc" class="ne-card-file">📎c1_adverb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491598-5c4ddfa8-bce2-4503-bf3b-a120bc3fed07.txt" id="u34728582" class="ne-card-file">📎c1_adverb_chapter2_26.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491703-1e8e8ec9-0f59-46af-9d56-fd2ab9f98ee5.txt" id="u391c40aa" class="ne-card-file">📎c1_noun_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491795-9a1ecd7e-1901-4b27-a3d2-e9859fcf8704.txt" id="u40513b10" class="ne-card-file">📎c1_noun_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491881-870d9e9b-44da-4e7e-abba-8d26465a5b62.txt" id="uf79cbca3" class="ne-card-file">📎c1_noun_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921491982-724450a6-b3d5-41f7-8c10-f881de90fbad.txt" id="ub295a1d7" class="ne-card-file">📎c1_noun_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492129-a1801363-de2f-4497-9b63-9aff315bea72.txt" id="ucf1a4084" class="ne-card-file">📎c1_noun_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492211-33e5e56b-38cd-45bb-abf8-e5c4c47220a9.txt" id="u07ef8f30" class="ne-card-file">📎c1_noun_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492354-789f193a-4590-4e33-9a9c-88aff94d3fc8.txt" id="ueb3b4e42" class="ne-card-file">📎c1_noun_chapter7_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492438-35c93765-8a84-45ef-b9b4-bcdd0e2ea858.txt" id="u64cc237e" class="ne-card-file">📎c1_noun_chapter8_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492513-7c10b952-8428-4f68-873e-4d13765534f5.txt" id="u35ea5853" class="ne-card-file">📎c1_noun_chapter9_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492573-e4415d1a-cb18-477b-bc46-3998d93a64d0.txt" id="udcc24541" class="ne-card-file">📎c1_noun_chapter10_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492651-b06815db-bc9c-4795-9fdf-ade59a6bb612.txt" id="udd038e24" class="ne-card-file">📎c1_noun_chapter11_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492767-540bab50-0ed1-4128-a7d3-cf873212275e.txt" id="ue6b539cb" class="ne-card-file">📎c1_noun_chapter12_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921492950-4923e758-134d-48a6-a24b-637c5482dfd6.txt" id="u096f34b8" class="ne-card-file">📎c1_noun_chapter13_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493055-6fd50702-b53e-48eb-88c2-91a8c9a12b62.txt" id="ua88ac26d" class="ne-card-file">📎c1_noun_chapter14_45.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493148-478d667c-6ed3-452f-a02b-cb1dcbfdd2d8.txt" id="u5a733ddd" class="ne-card-file">📎c1_other_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493244-473a392e-9bf0-4138-b0f3-08134b381586.txt" id="u3e3d23d8" class="ne-card-file">📎c1_other_chapter2_7.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493323-1fdd8ad6-533d-45a1-8bc1-e9c6b2b9d54e.txt" id="u7eb1fc80" class="ne-card-file">📎c1_verb_chapter1_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493397-a0370bee-1c02-4cf4-aee8-385b2129a7b4.txt" id="ud5c25d81" class="ne-card-file">📎c1_verb_chapter2_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493499-e21726a4-c2d8-4f4f-b1a1-8b6c2bcd52ee.txt" id="uc4c6d073" class="ne-card-file">📎c1_verb_chapter3_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493604-26cb088f-44ce-42ac-a13c-ee1f94129e54.txt" id="ue1d19ad3" class="ne-card-file">📎c1_verb_chapter4_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493722-25e63b96-6c0c-4cb3-8823-99a93700d2ff.txt" id="udbee9710" class="ne-card-file">📎c1_verb_chapter5_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493797-df88d216-8fc3-4187-96c1-9f63eff95879.txt" id="ub7a44e7e" class="ne-card-file">📎c1_verb_chapter6_50.txt</a><a href="https://www.yuque.com/attachments/yuque/0/2024/txt/21382055/1715921493903-e285e070-99d0-495b-888e-b999d9008417.txt" id="u46d592ba" class="ne-card-file">📎c1_verb_chapter7_19.txt</a></p></details>




<!-- 这是一张图片，ocr 内容为：无痕模式 IF-GRAY.XINXUAN818.COM/TOOL-LATFORM-HAOTIAN/#NISUALIZATION/DETAIL/SUPPLIER/供应商系统看板 更新 编程资源平台 2023.6.30.V1.供应... 个人文件管理 读书 娱乐 04-脚手架安装及... 导入中心 万子聪-V1 XX2 XX1 CACHE1 CACHE X 昊天埋点系统 17324865113 供应商系统看板 数据看板列表 西 访问指标概况 开始日期 结束日期 昨日近7天近30天 访问人数UV 人均停留时长 访问次数PV 442,246次 8,943次 访问指标概况 昨日近7天近30天 PV统计值 UV统计值 800 20000 梦想起 600 15000 10000 200 5000 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1693995805868-f60dcdaf-a245-42c5-8ed1-8aea858136d6.png)











