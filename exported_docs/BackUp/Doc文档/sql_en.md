

```plsql
-- demo.cerf_category definition

CREATE TABLE `cerf_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) DEFAULT NULL COMMENT '名字',
  `level` varchar(100) DEFAULT NULL COMMENT '分类级别',
  `desc` varchar(100) DEFAULT NULL COMMENT '分类中文描述',
  `code` varchar(100) DEFAULT NULL COMMENT '分类CODE',
  `parent_code` varchar(100) DEFAULT NULL COMMENT '父级别分类CODE',
  `leaf_count` int(11) DEFAULT NULL COMMENT '叶子节点数量',
  `children_count` int(11) DEFAULT NULL COMMENT '全部叶子节点数量',
  `custom_desc` varchar(100) DEFAULT NULL COMMENT '自定义描述信息',
  PRIMARY KEY (`id`),
  KEY `cerf_category_id_IDX` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='cerf_分类信息';


-- demo.cerf_words definition

CREATE TABLE `cerf_words` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) DEFAULT NULL COMMENT '单词内容',
  `level` varchar(100) DEFAULT NULL COMMENT '单词级别【a1 a2 a3 ...】【枚举】',
  `category_code_1` varchar(100) DEFAULT NULL COMMENT '单词1级分类',
  `category_code_2` varchar(100) DEFAULT NULL COMMENT '单词2级分类',
  `category_code_3` varchar(100) DEFAULT NULL COMMENT '单词3级分类',
  `type` varchar(100) DEFAULT NULL COMMENT '单词类型【单词、词组】【枚举】',
  `code` varchar(100) DEFAULT NULL COMMENT '单词CODE',
  `length` varchar(100) DEFAULT NULL COMMENT '单词长度',
  `start` varchar(100) DEFAULT NULL COMMENT '单词开头',
  `custom_desc` varchar(100) DEFAULT NULL COMMENT '自定义单词描述',
  `cx` varchar(100) DEFAULT NULL COMMENT '单词词性',
  `desc` varchar(100) DEFAULT NULL COMMENT '单词基本描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- demo.en_words definition

CREATE TABLE `en_words` (
  `word` varchar(32) NOT NULL DEFAULT '',
  `translation` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- demo.english_words definition

CREATE TABLE `english_words` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `chinese` varchar(128) DEFAULT NULL,
  `youdao_json` longtext COMMENT '有道',
  `jinsan_json` longtext,
  `length` int(11) DEFAULT NULL,
  `start` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `english_words_name_index` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=474128 DEFAULT CHARSET=utf8mb4 COMMENT='单词表';


-- demo.subtitle_sentence definition

CREATE TABLE `subtitle_sentence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sentence` text,
  `sentence_type` varchar(64) DEFAULT NULL,
  `chinese` text,
  `source_name` varchar(256) DEFAULT NULL,
  `source_path` varchar(256) DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `time_line` varchar(256) DEFAULT NULL,
  `sentence_type_enum` int(11) DEFAULT NULL,
  `sentence_length` int(11) DEFAULT NULL,
  `words_count` int(11) DEFAULT NULL COMMENT '句子单词长度范围',
  `trans_by_web` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18400 DEFAULT CHARSET=utf8mb4;
```

