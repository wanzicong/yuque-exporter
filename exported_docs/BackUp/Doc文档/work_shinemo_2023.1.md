荆门 token

client_id: fcf94779ef884cf786baa97be709c6fd

client_secret: 0a018a2baa1ccf8b4849ef48a438ca37c812a8644d2d40ef



荆门堡垒机登录appcube 账号和密码

[https://10.65.32.34/studio/index.html#/admin](https://10.65.32.34/studio/index.html#/admin)

账号AppCube_admin 

密码： Huawei123#$%

AppCube_cyzt    密码 Jmcsdn&013







```typescript
export class Organization {
    @action.param({ type: 'String', required: false, description: "机构名称，操作码为A时，必填；操作码为M时，选填；操作码为D时，不填", pattern: '^[^<>\'\"$]{0,64}$', message: '格式不合法' })
    orgName: string;
    @action.param({ type: 'String', required: true, description: "机构编码", pattern: '^[a-zA-Z0-9]([a-zA-Z0-9]{1,63})$', message: '格式不合法' })
    orgCode: string;
    @action.param({ type: 'String', required: false, description: "归属的区域编码，操作码为A时，必填；操作码为M时，选填；操作码为D时，不填", pattern: '^[a-zA-Z0-9]{0,63}$', message: '格式不合法' })
    regionCode: string;
    @action.param({ type: 'String[]', required: false, description: "管理的区域编码列表，操作码为A、M时，选填；操作码为D时，不填", message: '格式不合法' })
    manageRegionCodes: string[];
    @action.param({ type: 'String', required: false, description: "父区域编码，操作码为A、M时，选填；操作码为D时，不填", pattern: '^[a-zA-Z0-9]([a-zA-Z0-9]{0,63})$', message: '格式不合法' })
    pOrgCode: string;
    @action.param({ type: 'String', required: false, description: "父区域编码，操作码为A、M时，选填；操作码为D时，不填", pattern: '^(0|1|2)$', message: '格式不合法' })
    orgType: string;
    @action.param({ type: 'Position[]', required: false, description: "组织下的岗位，操作码为A、M时，选填；操作码为D时，不填", message: '格式不合法' })
    positions: object[];
    @action.param({ type: 'String', required: false, description: "组织描述，操作码为A、M时，选填；操作码为D时，不填", pattern: '^[^<>\'\"$]{0,64}$', message: '格式不合法' })
    description: string;
    @action.param({ type: 'String', required: true, description: "操作码，支持A：添加；M：修改；D：删除", pattern: '^(A|M|D)$', message: '格式不合法' })
    opCode: string;
    @action.param({ type: 'String', required: false, description: "组织下的管理领域，操作码为A、M时，选填；操作码为D时，不填", message: '格式不合法' })
    manageDomain: string;
    @action.param({ type: 'DutyRegion[]', required: false, description: "责任区域列表", message: '格式不合法' })
    dutyRegions: object[];
    @action.param({ type: 'OrganizationTag[]', required: false, description: "标签", message: '格式不合法' })
    tags: object[];
}
```







<!-- 这是一张图片，ocr 内容为：13 省级工单,城运一体化完成结宽审核,走了回访流程,应 目前通过省平台处理人处 ,应读直接 城运一体化与12345对接 一网统管,12345 开启 2023/1/6 |朱胜强 理完成可以完成案件办结 到12345终审:工单号:2023010600052 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673055473028-9c93efb0-54b3-4a89-b721-d84bc5acadfc.png)





<!-- 这是一张图片，ocr 内容为：12345普通工单市级,城运一体化处置部门进行拒签,流程走到 15 城运一体化与12345对接 开启 网统管 朱胜强 2023/1/6 16 了待结赛阶般 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673057776209-42d2a745-3087-4b92-957a-e4f1f602a7d3.png)



[https://www.kdocs.cn/l/cd435x1nX60Y](https://www.kdocs.cn/l/cd435x1nX60Y)



```sql
select  *   from ShineMo1__UOC001_C_TLD01__ItemDef__CST  where ShineMo1__customCode__CST = 'ZDJY001'


select * from SmartCity3__Category__CST where   id = 'cCj2000000x5w3x2lzKi'


select * from SmartCity3__Category__CST where   id  = 'cCj2000000x5v2u2Rlvk'


select * from SmartCity3__Category__CST where   id  = 'cCj2000000x5nLNF2bqK'    


select * from SmartCity3__Category__CST where   id  = 'cCj2000000x5n6vAWYrY'
```







<!-- 这是一张图片，ocr 内容为：02省级工单下派业务流程 200220240260280300320340 480 560 500 180 580 62 160 600 140 440 20 460 420 360 520 540 80 09 100  120 380 400 40 省审处贸员 省平台分拨员 市一缓承办单位 市一级分拨 区一般之 区一级分候 [别门行政审批局工作 人民日 市级分院可自行 谢亮辉 市承办单位办理 开始 工单业务流程 工单可引出 行生成 巡回工单 学理待分 省级工单 工学院承办综位各次 省级工单特派 对同可应用晚认贵性 按枚转派 脱回至市工单承办单位一 较刷至市工单示办单位一 直派市工单承办单位 市承办单位办理 不允许多滋御门 工单业务深程 省结案归 处置完提交结案 楼 结果申恢 姑果审核 区二级平台专 转滩区二级平台 工单办 源工单业务流 不允许多派御门 理流程 程 结束 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673078640545-c05b7348-a820-4acf-bc03-c973c5ac7e28.png)





<!-- 这是一张图片，ocr 内容为：重点-别门一网统管项 华为网惠民 20M 地图 相关附件 力理进度 历史推荐 工单编号:2023010700032 待处置 非自动分庆 即 修正记录 山导出PDF 上报 工单标题:道路拥堵 完成时间:2023-01-07 15:42:53 工单描述:[手动录入]的 分级 亲神英道:12345热线 具体来源:电话 瓶止时间: 完成时间:2023-01-07 16:15:23 澳通单号: 受理时间:2023-01-0715:42:53 处黄 诉求类型:智无 完成时间:2023-01-0716.28.58 截止时间: 诉家人类型:留无 处置 发生位置:湖北省用门市东宝区龙泉街道象山大道62号华铝广场 截止时间:一 亮成时间:2023-01-0716:18:41 品质标签: #日第工单 处置 钱止时间 办理部门:市城管局[市城管局-处置岗位] 事项信息 理时间:2023-01-0716:26:45 成分类:地市综合公共交通报道路交通管理 事项名称:交通拥难 工作:处蛋 食见:处置完成,请推查. 附件:A66C71ES-BE40-4990-A274-297695667C99.ONG 处留信息 处置部门:市交盛大队(主办)市受宣传部,市城管局 上景类型:主协办 发止时间:2023-01-0716:40:24 办法时间:2023-01-0716:16:24 处置后 处置前 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673080569271-2b4eea23-f780-43b9-95c9-13ff4545d418.png)





| <font style="color:rgb(51, 51, 51);">SmartCity3__CaseESUtil</font> | <font style="color:rgb(51, 51, 51);">脚本</font> | | |
| :--- | :--- | --- | --- |
| | <font style="color:rgb(51, 51, 51);">SmartCity3__DelayTaskAction</font> | <font style="color:rgb(51, 51, 51);">脚本</font> | |
| | <font style="color:rgb(51, 51, 51);">SmartCity3__ElasticsearchUtility</font> | | |






```typescript
[
    {
        "name": "小说",
        "value": "ojMGzeDmENKGVY6qWM9xR0AD3dy48zQe00p2bagZOrvLlojXnm7ek51BJ64nkVBL",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "悬疑推理",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw8qoJpzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "科幻",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbrdzPYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "世界名著",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzlYyp81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "中国名著",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPExXxQR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "军事战争",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMnyJwgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "武侠",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNGvDPgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "影视",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlyKMpYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "魔幻玄幻",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6ANVwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "职场",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQk8bvP1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "历史",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxBOzpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "社会",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQY9mlQOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "爱情婚恋",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnGKNwd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "近现代",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv6OXpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "当代",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rdeQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "中短篇作品",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRjL7prVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "长篇作品",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr7NNpVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "外国",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLogWwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            }
        ]
    },
    {
        "name": "影视原著",
        "value": "V5x4ydKZzoyMlbme6n0kBjqxrdXL9VQq6LPGOW4YJ87D3v1RZE5gNaAK22lAezN6",
        "sub_options": []
    },
    {
        "name": "心理学",
        "value": "Da1LVnd9dA74k9nB2G6YZrL8eqENW5Q47bpyaDO0RxV3lzK1vJjmboMXgregjymY",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "心理学通俗读物",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnMDgQd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "心理学与生活",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqMgbQGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "心理学理论",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0LzdQ71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "弗洛伊德",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pR6J7prVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "阿尔弗莱德·阿德勒",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp65b6wWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "儿童心理",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9gmdpKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "消费心理",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0MVdP71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "亲密关系",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw89EApzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "焦虑",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQenoWP2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "学习与记忆",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp759YPaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "思维方式",
                "value": "OGlLn3j657Mqz2vZ8AJ3VdB9NkWnaw5qmjwElGbO4KLgjro1mXRDeYy0xogKe7JD"
            },
            {
                "name": "自我认知",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0ERLP71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "情绪管理",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLKeDwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "人际交往",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQe7JWw2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "荣格",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVzmGP5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "心理学学派及分支",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pm2KEQ1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "教育心理学",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1aK2pje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "精神分析学派",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRzAEprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "社会心理学",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9zqdwKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "积极心理学",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4MvvPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "犯罪心理学",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqM7ZQGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            }
        ]
    },
    {
        "name": "历史",
        "value": "GKveNq0b0BdzylrD5j21qLJVXMReZnwA5Gw3EOm86GaWx7KgYA4b9okNvdoax4RB",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "历史通俗读物",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PW2B3QDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "历史学术著作",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPznjYP81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "历史自传他传",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxzjvpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "世界史",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQeek7Q2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "中国史",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgNkWP8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "思想史",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPErKxwR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "政治史",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4MAKPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "经济史",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP97A4pKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "战争史",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pR6BAprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "商业史",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMKdnpgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "科技史",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw85kypzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "哲学史",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmzeMQ1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "毛泽东",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLqjvQA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "拿破仑",
                "value": "OGlLn3j657Mqz2vZ8AJ3VdB9NkWnaw5jvEpElGbO4KLgjro1mXRDeYy0xogKe7JD"
            },
            {
                "name": "丘吉尔",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p18W7wje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "秦始皇",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmzaMQ1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "曾国藩",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1867wje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "蒋介石",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVkK0w5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "法国大革命",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlzl5QYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "第一次工业革命",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQe9lWQ2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "第二次工业革命",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pm7lOP1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "一战",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOedDwYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "二战",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKOdLpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "文艺复兴",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPV8dlp5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "中美关系",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbxvkpYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "古典时代",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRWbGQrVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "中世纪",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4jvOwyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "史前时期",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1NWkQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "夏商周",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRWJWQrVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "战国秦汉",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4jlewyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "三国",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3jWypAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "魏晋",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqydZQGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "南北朝",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgb32P8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "隋代",
                "value": "zNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPXb8GpWBLkg8Rvm24d9ObE3oJeM1o6jqnvK"
            },
            {
                "name": "唐代",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPozY9QgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "五代十国",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJdKOw92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "宋代",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp7ak3PaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "元代",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOWBMQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "明代",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDekKQ83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "清代",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp65q6wWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "近代",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJxybw92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "美国",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4mWbPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "英国",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3j7RpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "德国",
                "value": "Rnl4j9qXO4bAE8larL3DqoyBz5Wm0pa51ZpRn12ejvxK9GNYZM6JgVdk7kNKDGxe"
            },
            {
                "name": "日本",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp7mxVPaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "法国",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPV83Lp5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "印度",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0O6kp71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "中东",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwA2bBp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "俄罗斯",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPB2bDPLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "葡萄牙",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRW8EQrVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "西班牙",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4j5owyaDO0RxV3lzK1vJjmboMXgregjymY"
            }
        ]
    },
    {
        "name": "互联网",
        "value": "vGMV25XqgJ34YMo0L5laWVX2vx7RdkPyy2PmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "运营",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQkk1oQ1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "数据分析",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbxjLpYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "设计师",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2j0JwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "产品设计",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyMgxPmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "营销",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGZynQemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "互联网思维",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp653WwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "互联网前沿视野",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZvZyQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "中国互联网公司",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp7axzPaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "外国互联网公司",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDeOGQ83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "用户需求",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnzZNPd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "用户体验",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLKnvwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "商业模式",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr5AxPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "用户行为",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQkgXvQ1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "自媒体新媒体",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr0oNQVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "产品经理",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOW1DQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "新零售",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0O48p71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "互联网金融",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw8jKJQzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "互联网+",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQe72Ww2bagZOrvLlojXnm7ek51BJ64nkVBL"
            }
        ]
    },
    {
        "name": "商业",
        "value": "mldBNYWEA5mlBNjJGY0Rqzex2vWg97pm1mp1yrZaXdo8DKLEbn6M4kVO3jLX3zAv",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "商业通俗读物",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnMRaQd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "商业传记",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp7m8lPaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "商业理论",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p19VVpje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "商业案例与实务",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlMLLpYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "视野洞察",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvz7VpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "经营战略",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqNVlPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "领导力",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3EZRwAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "团队管理",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdbZNp9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "项目管理",
                "value": "gMjleDOrG8vZAkRX5yNnDzY1g69Wjwjo9xp0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ"
            },
            {
                "name": "商业模式",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyz3mwmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "新零售",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4maVPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "市场调研",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWxExwDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "企业竞争力",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzB5vP81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "投融资",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOW2bQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "创业",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAMOkw3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "企业创新",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbEJoQYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "中国企业及企业家",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pR6gKprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "外国企业及企业家",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoMmMpgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            }
        ]
    },
    {
        "name": "期刊杂志",
        "value": "V5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqZLPGOW4YJ87D3v1RZE5gNaAK22lAezN6",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "《看电影》",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4edvPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "《读者》",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9arJPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "《第一财经》",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnG1vwd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "《财经》",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv6RJpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "《环球人物》",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6Av7wWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "《哈佛商业评论》",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxBn7pm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "《读书》",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLonMwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "《当代》",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rRzQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "《中国国家天文》",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPExKOQR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "《21世纪商业评论》",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPExj8QR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "《商界》",
                "value": "zNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPXnM1pWBLkg8Rvm24d9ObE3oJeM1o6jqnvK"
            },
            {
                "name": "《证券市场周刊》",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQY9ZYQOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "《证券市场红周刊》",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQY9RJQOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "《中欧商业评论》",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rJ1Qje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "《天文爱好者》",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQee2AQ2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "《轻兵器》",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJoWKP92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "《北大金融评论》",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLoD4wA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "《散文》",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr7ZopVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "《小说月报》",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRjX9prVNbxD6B0M9konAXqYLyg576ONm5K"
            }
        ]
    },
    {
        "name": "管理学",
        "value": "Wk2YLJnemjblqYg7AM3Vo86EyRd4W9PWmjpDvOZkaGeL0zn1X52NKJBrx87lMXGd",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "企业经营与管理",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4MbePyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "管理通俗读物",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmMzEp1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "组织结构",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlMM9pYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "团队管理",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRxLWPrVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "品牌管理",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqX6ZpGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "创业",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr5kyPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "企业竞争力",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGnn6QemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "企业创新",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQkkygQ1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "物流与供应链",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0MMkP71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "战略管理",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvz0npXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "组织行为",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwra5yPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "企业文化",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoaN9pgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "明茨伯格",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQenAWP2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "德鲁克",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZv17Qv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "稻盛和夫",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPz3zOw81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "管理学大师",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzBDYP81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            }
        ]
    },
    {
        "name": "自我提升",
        "value": "YOe5lr9vlX9g2ae840VLG7o5ZDnBEMP9WvpKyYkqxNrzWOmd3b1JjRA6v4g830By",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "思维方式",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwArgvp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "说话沟通",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p19Kzpje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "学习方法",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw89GMpzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "精力管理",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGZ1AQemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "个人成长",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoyLZpgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "情绪管理",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgYk5Q8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "亲密关系",
                "value": "zNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPXDM2PWBLkg8Rvm24d9ObE3oJeM1o6jqnvK"
            },
            {
                "name": "时间管理",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGnEAQemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "职业技能",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6m66wWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "团队协作",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyzbvwmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "情商培养",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvzrKpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "职场写作",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw85DEpzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "职场新人",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPb2ddPYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "中层领导",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNxv5wgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "大学生",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyzyewmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "领导者",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6m3lwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            }
        ]
    },
    {
        "name": "科技",
        "value": "9bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQO1MwYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "科技公司",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGmoYpemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "科技前沿视野",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZ7rEPv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "科技与生活",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLK8MwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "科技关键词",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPB2rXPLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "科学家",
                "value": "zNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPX2R1pWBLkg8Rvm24d9ObE3oJeM1o6jqnvK"
            },
            {
                "name": "埃隆·马斯克",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLKrMwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "苹果",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPz36Ww81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "亚马逊",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9MNGPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "人工智能",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgY34Q8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "无人驾驶",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2jgowEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "大数据",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbxXzpYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "区块链",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNK2DPgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "比特币",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6mVVwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "物联网",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyza0wmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "互联网",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQYzjlPOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "基因编辑",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pR697prVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "5G",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p19xvpje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "芯片",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pR69JprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "脑机接口",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4mN5PyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "新能源",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0MJ9P71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "微软",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEraywR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "Facebook",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3bKBpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "谷歌",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9M9aPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "腾讯",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAMLvw3EOm86GaWx7KgYA4b9okNvdoax4RB"
            }
        ]
    },
    {
        "name": "经济",
        "value": "WGK0DgyEd6lkWmjXOZM4E7vbrDx1BKPorOQgL5RyeY93nNoqa0V8GzAJ28qrl16m",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "中国经济",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLKGvwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "经济学家",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw8jJyQzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            },
            {
                "name": "经济史",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PW20BQDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "经济学通俗读物",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMKe2pgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "诺贝尔奖",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLqODQA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "财政",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRjEGprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "货币",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZN8DQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "金融、银行",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQeeMWQ2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "保险",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4eyOPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "经济学经典著作",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxzVNpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "经济学应用",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEeZyPR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "经济危机",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwA2Evp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "贸易战",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZbBjQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "行为经济学",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2jagwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "政治经济学",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVlzYp5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "制度经济学",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv0Y9PXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "宏观经济学",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr5XoPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "微观经济学",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbEALQYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "芝加哥经济学派",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKKLgpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "奥地利经济学派",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNYzNpgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "凯恩斯学派",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKOqJpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "罗纳德·科斯",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNKqxPgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "亚当·斯密",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQY2aYPOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "大卫·李嘉图",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRWgAQrVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "哈耶克",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4javwyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "米尔顿·弗里德曼",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3jJBpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "美国经济",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9Mn4PKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "欧洲经济",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQk8GeP1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "世界各国经济概况",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJdR0w92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            }
        ]
    },
    {
        "name": "哲学与宗教",
        "value": "2BVeYxJznG01zjBXDxarZd4mNJL73gwg0kp8KqRvk2MWAOY9oEy6Vb5elljAERmN",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "思想经典",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3jYBpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "哲学理论",
                "value": "Rnl4j9qXO4bAE8larL3DqoyBz5Wm0paLGvwRn12ejvxK9GNYZM6JgVdk7kNKDGxe"
            },
            {
                "name": "哲学名家",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4jYKwyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "美学",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4eYOPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "中国哲学",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdZDqp9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "宗教",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAZYnp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "逻辑学",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVL8PGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "伦理学",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aX4PKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "诸子百家",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqy2EQGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "儒家思想",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pm76RP1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "禅宗",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4jGKwyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "道家思想",
                "value": "Rnl4j9qXO4bAE8larL3DqoyBz5Wm0pa5GxpRn12ejvxK9GNYZM6JgVdk7kNKDGxe"
            },
            {
                "name": "基督教",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmz9ZQ1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "佛教",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aXdPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "伊斯兰教",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoynVpgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "犹太教",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqXKGpGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "存在主义",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2jkdwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "现代哲学",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPBez5QLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "人生哲学",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rYnQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            }
        ]
    },
    {
        "name": "法律",
        "value": "MovAaOYqxZdaA2gR9B4NJLWkXYVmorpKWGpn0jO6q3e81GbylMEK5Dzv7dW4BGE6",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "法律通俗读物",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9775pKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "法律专著",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9MrVPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "司法解释",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGmmKpemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "经典案例",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgqq1Q8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "法条解读",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMnxnwgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "行政法",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdqq4w9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "民法",
                "value": "gMjleDOrG8vZAkRX5yNnDzY1g69WjwjNNaw0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ"
            },
            {
                "name": "刑法",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPznn9P81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "商法",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PW22ZQDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "经济法",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxzzbpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "诉讼法",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEeeGPR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "司法制度",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZbbLQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "婚姻法",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwA22qp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "刑事诉讼法",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyB62wmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "民事诉讼法",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxB9gpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "社会保障法",
                "value": "OGlLn3j657Mqz2vZ8AJ3VdB9NkWnaw5AKXwElGbO4KLgjro1mXRDeYy0xogKe7JD"
            },
            {
                "name": "行政诉讼法",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6AB7wWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "犯罪学",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv61JpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "法律思想",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPB2RvPLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "合同法",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnzMWPd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "知识产权",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlzMGQYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "物权法",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPylm0QmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "侵权责任",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxEAzwm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "债法",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwl02MwYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "英美法系",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKOKopn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "大陆法系",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPV8lAp5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            }
        ]
    },
    {
        "name": "传记",
        "value": "lyn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3oGQAXWdKanoreY4qkbMz3DG7m79jWxNM",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "历代帝王",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDxM2p83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "军事人物",
                "value": "zNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPXnKGpWBLkg8Rvm24d9ObE3oJeM1o6jqnvK"
            },
            {
                "name": "政治人物",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJoJOP92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "财经人物",
                "value": "Rnl4j9qXO4bAE8larL3DqoyBz5Wm0paLAvwRn12ejvxK9GNYZM6JgVdk7kNKDGxe"
            },
            {
                "name": "科学家",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbrYEPYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "宗教人物",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPBeZ5QLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "女性人物",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2RkxwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "艺术家",
                "value": "gMjleDOrG8vZAkRX5yNnDzY1g69Wjwj9e9P0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ"
            },
            {
                "name": "文学家",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQk84OP1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "学者",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNG5aPgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            }
        ]
    },
    {
        "name": "社会学",
        "value": "rA8XdO46oA1E4kLX6gvl3MyJxzD7dWPGWBPemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "社会学理论著作",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPznqvP81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "社会热点问题",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pm7d3P1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "社会观察",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxzA1pm8vb3yB92zO51kMX0eNoWnBrgjY97"
            },
            {
                "name": "社会调查",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PW2eNQDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "中国",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgbKlP8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "社会变迁",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4jdLwyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "社会生活与社会问题",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnMmWQd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "社会心理与社会行为",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgYj1Q8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "前沿视野",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEe7kPR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "城市化",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQkMe6w1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "个人和社会",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6RwraEMPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            }
        ]
    },
    {
        "name": "文学",
        "value": "Dmga0zrA2zyY6a179NgLJD3lkEd84WPVA0Q5eMnrGZxomBvRj0XVbOqAK6neZvY9",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "世界名著",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQYz5oPOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "中国古代文学名家及作品",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzBz9P81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "诺贝尔文学奖",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOA2ewYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "中国现当代文学名家及作品",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWx4ZwDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "国学经典",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqN1ZPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "文学名家及作品",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQYzm0POgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "文学评论及鉴赏",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqNdWPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "文学理论",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdZzMp9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "文学史",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbrazPYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "小说",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQYzZEPOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "诗歌词曲",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMngJwgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "散文随笔杂文",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNGyDPgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "传记",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoMb9pgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "回忆录",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPylvOQmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "纪实文学",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6AxVwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "戏剧曲艺",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWlWzwDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "茅盾文学奖",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPb2YlPYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            }
        ]
    },
    {
        "name": "计算机",
        "value": "r0V7k1e220gRNB3DGL8rjkYMedEV7bp77rpaKzmlXO416vA9yn5WJqZxoyJDZA3o",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "编程开发",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr76NpVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "计算机理论",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwly6MpYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "数据库",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRj77prVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "软件工程",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZN1WQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "信息系统",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aDVPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "人工智能",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv6VbpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "多媒体",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rgeQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "网络通讯",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQee6XQ2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "操作系统",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLo2WwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "硬件开发",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAZGlp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "电子商务",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rgvQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "IT产业",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLo2EwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "安全加密",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmg6qP1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "行业软件",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVoWPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            }
        ]
    },
    {
        "name": "自然科学总论",
        "value": "zOGlLn3j657Mqz2vZ8AJ3VdB9NkWnaw5MWwElGbO4KLgjro1mXRDeYy0xogKe7JD",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "诺贝尔奖",
                "value": "Rnl4j9qXO4bAE8larL3DqoyBz5Wm0panAmQRn12ejvxK9GNYZM6JgVdk7kNKDGxe"
            },
            {
                "name": "自然科学理论著作",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6aMVwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "科学史",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqN3GPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "科普",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPylavQmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "科学哲学",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPz3vWw81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "科学思维",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRx49PrVNbxD6B0M9konAXqYLyg576ONm5K"
            }
        ]
    },
    {
        "name": "数理科学与化学",
        "value": "0Rnl4j9qXO4bAE8larL3DqoyBz5Wm0pajyQRn12ejvxK9GNYZM6JgVdk7kNKDGxe",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "数学",
                "value": "gMjleDOrG8vZAkRX5yNnDzY1g69Wjwj9WJP0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ"
            },
            {
                "name": "物理学",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRjZWprVNbxD6B0M9konAXqYLyg576ONm5K"
            }
        ]
    },
    {
        "name": "生物科学",
        "value": "rXAl15znMexOnqb2XlYzokEyJ95gvApDWXw83DNRZr6KVGLaW170dmjB4EOmBk6W",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "细胞生物学",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDxK0p83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "遗传学",
                "value": "K86kabNoONLMJbDGVZvW0EzqBmrdYQ0LbBQ71y2geK9k43xRXA8j65lanO2eDv53"
            },
            {
                "name": "生理学",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQk8l6P1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "生物化学",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLoEewA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "分子生物学",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2RJRwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "古生物学",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyBvewmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "微生物学",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr731pVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "植物学",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr73MpVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "动物学",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3ZWepAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "昆虫学",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdZnep9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "人类学",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlyd3pYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "生态学",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3ZLXpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            }
        ]
    },
    {
        "name": "医药与卫生",
        "value": "JK86kabNoONLMJbDGVZvW0EzqBmrdYQ0o3p71y2geK9k43xRXA8j65lanO2eDv53",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "一般理论",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmgZ3P1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "研究方法",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKobopn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "预防医学与卫生学",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3ZlepAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "基础医学",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzlVvp81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "临床医学",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLobOwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "内科学",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAZajp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "外科学",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4eAbPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "妇产科学",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKoZGpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "儿科学",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDxXXp83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "肿瘤学",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdZRop9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "神经病学与精神病学",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPExynQR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "皮肤病学与性病学",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLo8KwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "耳鼻咽喉科学",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZNRXQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "眼科学",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aJvPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "口腔科学",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVkE0w5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "特种医学",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPBeWOQLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "药学",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzlm5p81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            }
        ]
    },
    {
        "name": "天文与地球科学",
        "value": "azNWRM4Ll7Nr0VaAqyDYX5zjnZxG6KPXMowWBLkg8Rvm24d9ObE3oJeM1o6jqnvK",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "天文学科普",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWloxwDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "天文观测",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnG3awd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "宇宙学",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv6bVpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "太阳系",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr7bnpVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "天文学",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPzlNDp81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "地球物理学",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgNm4P8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "大气科学",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVkOLw5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "海洋学",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rv2Qje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            }
        ]
    },
    {
        "name": "艺术",
        "value": "aBAjYy4g0BM8Zqgkj34NR5r1dVznlOQJWYP92xGbXvAW6mJYDEeL7oaKy0W8OX5Z",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "艺术理论",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr763pVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "艺术史",
                "value": "oEJz13njdG7eW2E1RKOZ3azl8mvJ4pRj7JprVNbxD6B0M9konAXqYLyg576ONm5K"
            },
            {
                "name": "世界艺术",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZN1yQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "绘画",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4eg5PyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "音乐",
                "value": "A8XdO46oA1E4kLX6gvl3MyJxzD7dWPGx5rwemYR8B52Kbqj0GnrV9ZaNOVDJBZ5a"
            },
            {
                "name": "设计",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVo8PGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "影视",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aD4PKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "动画",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOo7XQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "戏剧",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoy67pgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "摄影",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgNx2P8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "雕塑",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKolrpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "建筑",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3ZMDpAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "舞蹈",
                "value": "mga0zrA2zyY6a179NgLJD3lkEd84WPVkxDw5eMnrGZxomBvRj0XVbOqAK6neZvY9"
            },
            {
                "name": "工艺美术",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp76DKwaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            }
        ]
    },
    {
        "name": "人类学",
        "value": "5DV4A8d9KVNA1mGBl865q2LodxzODWw2lvQEnYMe4J3y9bav7kgRrjX0ZbvlyYZk",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "人类学经典著作及理论",
                "value": "JVmd7ENd8VkK9q47eg6yM52nRGABlPbxgdpYmO31jNabZDLXrE0JzoxvWMxzjZ1L"
            },
            {
                "name": "人类学通俗读物",
                "value": "9JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNKX5Pgbd2XZaNKR3WnE07JMkDGoWz2vrKD"
            },
            {
                "name": "文化史",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6BvlpWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "语言学",
                "value": "WXZmORLB8y6rvYLAjdkRnG9z7ZbmDQYzNWPOgqXMo1exW2J43Kl5Na0VEde3rb9a"
            },
            {
                "name": "符号学",
                "value": "XM5znRl8EvXy3JzY5o7mnqbkWRj4DQkg76Q1dAVNOraeM2Bl69LK0gxZGB4y3gj0"
            },
            {
                "name": "婚姻",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOeNgwYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "性别",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKOYMpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "宗教",
                "value": "DV4A8d9KVNA1mGBl865q2LodxzODWw2jBRwEnYMe4J3y9bav7kgRrjX0ZbvlyYZk"
            },
            {
                "name": "民俗学",
                "value": "X5j6m723vNJLRaW7lq120Gdk5o9nZPMxN3QgYEKmBAD8eVMjy6r4OXzxbZMYzkE1"
            },
            {
                "name": "文化",
                "value": "41qMkRzRl6JroAWby258BMe74jOnVwlz5GQYqGxKazL0g9D3NdmvZkEX10Ny5BXJ"
            },
            {
                "name": "考古学",
                "value": "dajqNV8bKrZMqG8l0mBEN6aok9g7Vw8jE0QzOy35XeWv1nAJxRj2D4dLY7RBgE0l"
            }
        ]
    },
    {
        "name": "教育",
        "value": "EarxJjZvJvglXA63Bq5y2NRrbZdMOxPB0OpLVkK4z8aWjG9ome0Y17EnDoGy5NDl",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "教育心理",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqNZrPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "学习方法与自学",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoMrepgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            },
            {
                "name": "世界各国教育事业",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZv7WQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "幼儿教育",
                "value": "XAl15znMexOnqb2XlYzokEyJ95gvApDAy0Q83DNRZr6KVGLaW170dmjB4EOmBk6W"
            },
            {
                "name": "初等教育",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJngnQ92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "成人教育",
                "value": "78W2k53rVGE3Az5JXRKNg0yvZnMDOPz3nyw81LqW6d9Bl2m7kxaejYb4odqO4Ejg"
            },
            {
                "name": "高等教育",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWbxzQDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "青少年",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqXmEpGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "家庭教育",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmzZRQ1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "亲子关系",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9MxGPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "教师与学生",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOWyOQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            }
        ]
    },
    {
        "name": "军事",
        "value": "5dajqNV8bKrZMqG8l0mBEN6aok9g7Vw8onPzOy35XeWv1nAJxRj2D4dLY7RBgE0l",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "一战",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3jZepAXWdKanoreY4qkbMz3DG7m79jWxNM"
            },
            {
                "name": "二战",
                "value": "0V7k1e220gRNB3DGL8rjkYMedEV7bp7a6lPaKzmlXO416vA9yn5WJqZxoyJDZA3o"
            },
            {
                "name": "抗日战争",
                "value": "BAjYy4g0BM8Zqgkj34NR5r1dVznlOQJxo6w92xGbXvAW6mJYDEeL7oaKy0W8OX5Z"
            },
            {
                "name": "冷战",
                "value": "0DYv3aWon714NWZYkOJa8vRbmVy5ePdqZew9rx3LzBK6MjX0lG2gqdAEDJ91mBjb"
            },
            {
                "name": "美国内战",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEexkPR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "国共内战",
                "value": "gMjleDOrG8vZAkRX5yNnDzY1g69WjwjGD2p0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ"
            },
            {
                "name": "军事理论",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv68jpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "军事史",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1rlnQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "世界军事",
                "value": "W25MJyb4A32EvOeJdrYMb0jz9o7GNPEeYnPR5ZgX1DL8lq6xnKWaVBmkyVrEG6Yl"
            },
            {
                "name": "中国军事",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLo3vwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "战略战役战术",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr7nxpVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "军事技术",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVnbPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            }
        ]
    },
    {
        "name": "传播学",
        "value": "K0DYv3aWon714NWZYkOJa8vRbmVy5ePd0oP9rx3LzBK6MjX0lG2gqdAEDJ91mBjb",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "新媒体自媒体",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p19Gnpje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "信息与传播理论",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAZlnp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "新闻学",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmgyOP1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "广播电视事业",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVYbPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "出版事业",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9aldPKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "图书馆学",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1r1kQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "博物馆学",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLoyJwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "档案学",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr7KypVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            }
        ]
    },
    {
        "name": "语言与文字",
        "value": "lJVmd7ENd8VkK9q47eg6yM52nRGABlPbdDpYmO31jNabZDLXrE0JzoxvWMxzjZ1L",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "语言学",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKo62pn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            },
            {
                "name": "汉语",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPBe6DQLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            }
        ]
    },
    {
        "name": "地理",
        "value": "KXM5znRl8EvXy3JzY5o7mnqbkWRj4DQkbep1dAVNOraeM2Bl69LK0gxZGB4y3gj0",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "历史地理学",
                "value": "arxJjZvJvglXA63Bq5y2NRrbZdMOxPBvWoPLVkK4z8aWjG9ome0Y17EnDoGy5NDl"
            },
            {
                "name": "亚洲",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv0aGPXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "非洲",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p18OVwje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "南美洲",
                "value": "YX2AkgVnaYGA08yjmlL2gBqx1Oo6Rwr5oMPVdKeDN3J4bkEZv5rM9z7WXyZ0vOdL"
            },
            {
                "name": "大洋洲",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZvAzQv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "欧洲",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQe7bVw2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "各国地理",
                "value": "yn2d86X5lJE2jO0gv6LVyN9B1xRZ8Q3ZvypAXWdKanoreY4qkbMz3DG7m79jWxNM"
            }
        ]
    },
    {
        "name": "体育与运动",
        "value": "VgMjleDOrG8vZAkRX5yNnDzY1g69WjwjYzP0bJMEx7LmeO2qdBoVl4aK3RJAEoGZ",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "体育理论",
                "value": "N7r0xXAOk346rqanZE8Y7xGR2oVbWQZNE7Qv5KyeB1lDN90JmzXLMjdgA8baRK53"
            },
            {
                "name": "世界各国体育",
                "value": "jMGzeDmENKGVY6qWM9xR0AD3dy48zQeeL7Q2bagZOrvLlojXnm7ek51BJ64nkVBL"
            },
            {
                "name": "田径运动",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4eRePyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "体操运动",
                "value": "KveNq0b0BdzylrD5j21qLJVXMReZnwAZ6Bp3EOm86GaWx7KgYA4b9okNvdoax4RB"
            },
            {
                "name": "球类运动",
                "value": "ldBNYWEA5mlBNjJGY0Rqzex2vWg97pmgqEP1yrZaXdo8DKLEbn6M4kVO3jLX3zAv"
            },
            {
                "name": "武术及民族形式体育",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqVgZPGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "水上、冰雪运动",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9am6PKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "其他体育运动",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOo67QYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "文体运动",
                "value": "GK0DgyEd6lkWmjXOZM4E7vbrDx1BKPoyO9pgL5RyeY93nNoqa0V8GzAJ28qrl16m"
            }
        ]
    },
    {
        "name": "英文电子书",
        "value": "NXlMz39On6Bra7byEl80DLdm4zo1AVp632QWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
    },
    {
        "name": "经典套系",
        "value": "vlKVA68nNWjlrgnGRKax0B2O5Db8J3PnL2pd6kqV1XymoA7zZ49LevYMEZ5JL9kj",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "经典套系",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv6NJpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "中华经典藏书",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1ra1Qje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "汉译名著",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLoz4wA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            },
            {
                "name": "全本全注全译丛书",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4e3vPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "皮书",
                "value": "a1LVnd9dA74k9nB2G6YZrL8eqENW5Q4emvPyaDO0RxV3lzK1vJjmboMXgregjymY"
            },
            {
                "name": "大辞海",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv669pXEBOlvko9L026gdm3AnGNMDkG1x8J"
            }
        ]
    },
    {
        "name": "少儿",
        "value": "B78W2k53rVGE3Az5JXRKNg0yvZnMDOPzY5Q81LqW6d9Bl2m7kxaejYb4odqO4Ejg",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "儿童文学",
                "value": "9vmWzAl54WYrJ78ayq1VjKbDeZRxzpv62bpXEBOlvko9L026gdm3AnGNMDkG1x8J"
            },
            {
                "name": "漫画绘本",
                "value": "yJdeKqvNJKmXr9WZyGB2aEOLlvYz6p1r2vQje3n8Ro1Db05kA7qdMV4xgroWEMNL"
            },
            {
                "name": "科普百科",
                "value": "W6obgA3DGqz14MWYyXl5ar29KxebnpLolEwA3EB8LOR6ZgmNk0voJj7dVJa9mXlq"
            }
        ]
    },
    {
        "name": "动漫绘本",
        "value": "89JYX4ajLrYe9xqlvBA8jm5yO16Vz4QNvqQgbd2XZaNKR3WnE07JMkDGoWz2vrKD",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "绘本",
                "value": "XlMz39On6Bra7byEl80DLdm4zo1AVp6AMxwWZO2XegvK3kRGNqj9xM5YJYd2eJr4"
            },
            {
                "name": "大陆漫画",
                "value": "k2YLJnemjblqYg7AM3Vo86EyRd4W9PWl33wDvOZkaGeL0zn1X52NKJBrx87lMXGd"
            },
            {
                "name": "港台漫画",
                "value": "lKVA68nNWjlrgnGRKax0B2O5Db8J3PnGqywd6kqV1XymoA7zZ49LevYMEZ5JL9kj"
            },
            {
                "name": "日韩漫画",
                "value": "GMV25XqgJ34YMo0L5laWVX2vx7RdkPyBENwmnEq1ZBy6KNbGjeDzOA9r8ydWjD9Y"
            },
            {
                "name": "欧美漫画",
                "value": "xlovK1bLAZxVRdEr46lK7GYJDjagqPxB2vpm8vb3yB92zO51kMX0eNoWnBrgjY97"
            }
        ]
    },
    {
        "name": "旅游",
        "value": "0X5j6m723vNJLRaW7lq120Gdk5o9nZPMyWPgYEKmBAD8eVMjy6r4OXzxbZMYzkE1",
        "sub_options": [
            {
                "name": "全部",
                "value": "X9vmWzAl54WYrJ78ayq1VjKbDeZRxzpvnpXEBOlvko9L026gdm3AnGNMDkG1x8JR"
            },
            {
                "name": "旅游随笔",
                "value": "5x4ydKZzoyMlbme6n0kBjqxrdXL9VQqV28PGOW4YJ87D3v1RZE5gNaAK22lAezN6"
            },
            {
                "name": "国内游",
                "value": "Oe5lr9vlX9g2ae840VLG7o5ZDnBEMP9ay4PKyYkqxNrzWOmd3b1JjRA6v4g830By"
            },
            {
                "name": "国外游",
                "value": "bZyoDzAEkMKRVd3yD6nNxJLeOgr9oQOo2XQYZ0Xm4Aql285Ba7jvGz1bWl0d6YnR"
            },
            {
                "name": "户外探险",
                "value": "BVeYxJznG01zjBXDxarZd4mNJL73gwgNr2P8KqRvk2MWAOY9oEy6Vb5elljAERmN"
            },
            {
                "name": "旅游摄影",
                "value": "ovAaOYqxZdaA2gR9B4NJLWkXYVmorpKoXrpn0jO6q3e81GbylMEK5Dzv7dW4BGE6"
            }
        ]
    }
]
```





[https://www.kdocs.cn/l/cpVdQbLZ3Hqf](https://www.kdocs.cn/l/cpVdQbLZ3Hqf)





<details class="lake-collapse"><summary id="u331c491a"><span class="ne-text">终止需求方案</span></summary><p id="u65862547" class="ne-p"><span class="ne-text"></span></p><p id="u0e51ff32" class="ne-p"><span class="ne-text">1 场景描述： 在流程中任务执行人任务执行完毕后生成新的代办任务，比如分拨员分拨后生成新的待处置任务，当前阶段是处于待处置状态，分拨员想终止当前的事件，分拨员执行终止操作后全部的代办任务关闭同时事件的状态是终止状态。</span></p><p id="u65222b44" class="ne-p"><span class="ne-text"></span></p><p id="ua70b9148" class="ne-p"><span class="ne-text">2 技术设计方案：</span></p><p id="u10c30b4b" class="ne-p"><span class="ne-text">2.1 实现逻辑： 基于上面描述的场景，分拨员通过调用changecasestatus接口 同时传入的action 为terminate，保证当前操作进行下去的限制逻辑为，1. 当前待处置阶段的流程节点配置了允许操作为 terminate 2 传入的handlinguser操作人的信息必须是分拨员，传入处置人的信息进行终止操作是不被允许的，这一点特别注意！</span></p><p id="u0768ecf6" class="ne-p"><span class="ne-text">2.1 技术实现逻辑：基于现有的接口changecasestatus接口，修改原有的操作逻辑。代码的逻辑为，如果接口传入的action为 terminate 就执行当前需求需要的限制逻辑，判断当前当前阶段是否配置了允许 terminate操作，如果没有配置提示用户当前操作不被允许，如果当前阶段配置了action terminate，继续判断当前操作人是否是为分拨员，就是当前代办任务的上一步操作人，如果前两个限制能过去的话，走底层terminatetaskaction的逻辑，判断当前事件是否有已经为关闭状态和当前事件是否还有代办任务，如果满足条件，将全部的代办任务的状态修改为terminated ，将事件的状态为 terminated，同时记录一条分拨人员的终止经办记录，改记录记录在分拨任务经办记录的业务字段中。</span></p><p id="u08b77981" class="ne-p"><span class="ne-text"></span></p><p id="u8d8ecf6b" class="ne-p"><span class="ne-text"></span></p></details>




任红对接：

[https://pms.shinemo.com/project-task-158-unclosed-0-name_asc-23-100.html](https://pms.shinemo.com/project-task-158-unclosed-0-name_asc-23-100.html)

[https://wiki.shinemo.com/pages/viewpage.action?pageId=97341795](https://wiki.shinemo.com/pages/viewpage.action?pageId=97341795)





<!-- 这是一张图片，ocr 内容为：巡查中心服... 进行中 3.5 16 18% 心曹仁红 4621 低 0 未开始 0 子检查项管理 曹仁红 0 0% 低 4675 子采巡事项管理 0 未开始 0 0 曹仁红 0% 4674 低 0 0 0 未开始 子采巡任务管理 0% 曹仁红 低 4677 子采巡分类管理 进行中 0 3.5 16 18% 曹仁红 低 4673 0 0 O 采巡计划管理 0% 未开始 曹仁红 低 4676 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673319282920-45bd96ac-7772-446c-918e-fb0a03fe7180.png)





<!-- 这是一张图片，ocr 内容为：巡查中心服.. 检查项管理 采巡事项管理 采巡任务管理 采巡分类管理 采巡计划管理 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673319538403-9890a233-6782-4326-b877-2f2e23eb8a9c.png)   <font style="color:#E8323C;"> </font>**<font style="color:#E8323C;">巡查分类  巡查事项  检查事项</font>****   ****<font style="color:#601BDE;">巡查计划 巡查任务</font>**





荆门bug

市级12345上报-市下派区-区下派街道分拨中心

-街道分拨-街道处置-街道办结

-市级办结-市办结

-12345回访 退回重办-区分拨中心签收



上报参数： 



```typescript
{ 
    "address": "荆门市", 
    "attachments": [ 
        { 
            "attachmentName": "希望同志们大力弘扬留学报国的光荣传统，以报效国家、服务以报效国家、服务服务以报效国家、服务学报国的光荣传统.pdf", 
            "attachmentUrl": "instance/upload/6e447f30-e659-4547-8ecb-ed716a361b3f__希望同志们大力弘扬留学报国的光荣传统，以报效国家、服务以报效国家、服务服务以报效国家、服务学报国的光荣传统.pdf" 
        } 
    ], 
    "caseName": "荆门测试", 
    "caseType": "2", 
    "channelId": "AAA", 
    "channelType": "005", 
    "comment": "string", 
    "description": "", 
    "cityCode": "420800000000", 
    "districtCode": "420802", 
    "communityCode": "420802001006", 
    "demanderType":"诉求人类型", 
    "demandType":"诉求类型", 
    "enterpriseProblemClassify":"企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类企业问题分类", 
    "handlingUser": { 
        "orgCode": "ORGAN983914976466964480", 
        "orgName": "荆门市城运中心", 
        "postCode": "JOB984491254467268608", 
        "postName": "市城运中心受理岗", 
        "userCode": "8a91b7bd814785580181478c74c20016", 
        "userName": "lty" 
    }, 
    "extFieldValues": [ 
        { 
            "fieldName": "Enterprisename", 
            "fieldValue": "鲁班七号大集团" 
        }, 
        { 
            "fieldName": "UscCode", 
            "fieldValue": "8888888888" 
        }, 
        { 
            "fieldName": "DocumentType", 
            "fieldValue": "身份证" 
        }, 
        { 
            "fieldName": "CertificateID", 
            "fieldValue": "362502188888888888" 
        } 

    ], 
    "itemCode": "JM0099", 
    "latitude": "112.12", 
    "longitude": "31.02", 
    "occurrenceDate": "2022-07-17 10:00:00", 
    "reportPersonalInfo": { 
        "contactName": "李四", 
        "mobilePhone": "18876711154675", 
        "needReVisit": "Y", 
        "Telephone": "13767401249", 
        "needProtected": "Y" 
    }, 
    "severityLevel": "3", 
    "srcCaseId": "", 
    "streetCode": "", 
    "tagCodes": [], 
    "urgencyLevel": "3" 
}


"caseCode": "2023011000010",


下派： https://dev.intouchmarket.huawei.com/service/SmartCity3__CaseService/1.0.0/DelegateCase
{
    "handlingUser": {
        "orgCode": "chanchengqufenbozhongxin",
        "orgName": "禅城区分拨中心",
        "postCode": "chanchengqufenbozhongxinzuoxiyuan",
        "postName": "禅城区分拨中心坐席员",
        "userCode": "wangminjie",
        "userName": "wangminjie"
    },
    "caseCode": "2022102800060",
    "regionCode": "nanzhuangzhenjiedaochenguanzhongdui",
    "comment": "事件下派到南庄镇分拨中心"
}



{
    "attachments": [],
    "caseCode": "2023011000010",
    "comment": "下派",
    "handlingUser": {
        "orgCode": "ORGAN983914976466964480",
        "orgName": "荆门市城运中心",
        "postCode": "JOB984495601519431680",
        "postName": "市城运中心派遣岗",
        "userCode": "8a91b7bd81478558018147b2878900a0",
        "userName": "wjw"
    },
    "reason": "下派",
    "regionCode": "420802"
} 
谢亮辉
{
    "attachments": [],
    "caseCode": "2023011000010",
    "comment": "下派",
    "handlingUser": {
        "orgCode": "ORGAN983917862051647488",
        "orgName": "东宝区城运中心",
        "postCode": "JOB984501174654734336",
        "postName": "东宝区城运中心派遣员",
        "userCode": "8a91b7bd81478558018147d93dda0126",
        "userName": "tqs"
    },
    "reason": "下派",
    "regionCode": "420802001"
} 



市级上报 "itemCode": "JM0099",交通管理 市级下派后，不会生成待签收任务

好的itemcode "FSLJ001"

```





<!-- 这是一张图片，ocr 内容为：SHINE 发布版本/5布局定义 模型定义/2对象定义 义/3字段定义 编排布局 领域模型树 模型配置指南:可以在左例树结构下根据不同层级需求,按此步裂以此来配置相应的领域模型 领域模型树,按照城运中台进行划分.展 示业务及领域下的实例模型 默认字段 自定义字段 对象信息 当前用户:禅城区城运治理中心 服务配置 DWWESFEF 自定义字段(显示对象下的言定义字象) FRFRHTHYH +新增字段 事项目录 首页 测试事项分类 字段名称 大小写敏感 宇段编码 操作 必须 索引 最近修... 宇段类型 数据类型 TT1 领域及模型配置 CRH开发分类 否 否 自定义字段 文本 WANZICONG 2023-01-1... WANZICONG 业务管理 WANGJLE 否 否 否 防汛副指... 2023-01-1 自定义字段 FLOODPREV... 文本 WANGJIE领... 领域管理 扩展 事件模型管理 门防汛副... 默认模型管理 T WANZI... ACHENTEST 领域模型管理 HWH事项分类 目 选项列表 CAK测试分类 YP测试分类 空 编码规则 事项配置 123123123 全球比最强还... 流程配置 测试新增 ZCC开发分类 城运中心 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1673417472858-e99f6e66-b8ba-484c-abf4-97bcd755dcf6.png)





| <font style="color:rgb(51, 51, 51);">SmartCity3__CaseESUtil</font> | <font style="color:rgb(51, 51, 51);">脚本</font> | | |
| :--- | :--- | --- | --- |
| <font style="color:rgb(51, 51, 51);">SmartCity3__CaseESUtil</font><br/><font style="color:rgb(51, 51, 51);">SmartCity3__DelayTaskAction</font><br/><font style="color:rgb(51, 51, 51);">SmartCity3__ElasticsearchUtility</font> | <font style="color:rgb(51, 51, 51);">SmartCity3__DelayTaskAction</font> | <font style="color:rgb(51, 51, 51);">脚本</font> | |
| | <font style="color:rgb(51, 51, 51);">SmartCity3__ElasticsearchUtility</font> | | |




| <font style="color:rgb(51, 51, 51);">SmartCity3__DelayCase</font> | <font style="color:rgb(51, 51, 51);">脚本</font> | |
| :--- | :--- | --- |
| | <font style="color:rgb(51, 51, 51);">SmartCity3__DelayCaseV2</font> | |






年前遗留问题清单： 

[https://www.kdocs.cn/l/cpVdQbLZ3Hqf](https://www.kdocs.cn/l/cpVdQbLZ3Hqf)



<!-- 这是一张图片，ocr 内容为：审核流转到监管岗,应该流转派道岗,监管阅义没有该菜单,市级审核元欧流程死掉 33 12345普通工单-镇街;区派遣在申诉列表中找不到申诉工单;工单编号: 严五 开启 网统管与12345对接 朱胜强 网统管,12345 2023/1/14 2023011400002 荆门项目需求:不满意申诉适配12345的一级分拨组织,仅市直一级部门和各区县发起 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1675216043467-f59eec79-2552-42a9-bce6-a19e6b26f555.png)





<!-- 这是一张图片，ocr 内容为：问题场景:市级12345上报-市级下派给区级-区级分拨-区级处置- 区级办结-市级办结-市级回访 需要通过QUERYCASES查询出 现在区级分拨需要进行满意度申诉, 不满意的工单, 人参为: QUERYCASECOND": ADA TATMRUN STATUSES": 已办结 13456 TASKQUERYCOND": [ "EXTFIELDVALUES":[ "RESULT", "FIELDNAME "FIELDYALUE":"1" "FIELDNAME":"RESULT", "FIELDVALUE":"2" 子 1. HANDLEDPOSTCODES J0B984491254467268608 CHANNELTYPES":[ 004 1 8 PAGING": PAGENUM:1, PAGESIZE":10 "HANDLINGUSER":[ ORGCODE":"ORGAN983917030782537728", "ORGNAME":"民政局", "POSTCODE":"JOB984500729869766656", "东宝区-民政局-处置岗", POSTNAME":"东 "赵丽颖", USERNAME "USERCODE":"ZLY" 修改意见::将"HANDLEDPOSTCODES":[ "JOB984491254467268608" 入参 不要全匹配 23 或者技术设计一下,如何能实现目前需求,在不影响老功能情况 下 1.入参中的"TASKQUERYCOND":传入的是区级分拨岗,或者市 级分拨岗的数据 不支持原因:(如果需要支持,需要提需求) 1.TASKQUERYCOND里面的查询条件都是并且关系,全匹配才 能查询到 -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1675217360485-ece94501-0687-4426-9d1a-50508a0521c7.png)







