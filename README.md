# CPPObserver
CPP票务观察小脚本

| 依赖需求     | 链接 | 重要性 | 功能      |
|----------|----|-----|---------|
| EasyQQ   |    | 二选一 | QQ机器人提醒 |
| EasyMail |    | 二选一 | 邮件提醒功能  |


运行后会生成config.json配置文件

配置文件项目解释如下

| 文件项目                  | 类型     | 描述                      |
|-----------------------|--------|-------------------------|
| eula                  | bool   | 同意用户许可协议                |
| cookies               | string | 用户cookies（自行获取并填入，必填）   |
| botEnable             | bool   | 是否启用QQ机器人功能（需要搭配EasyQQ） |
| botAddress            | string | EasyQQAPI地址             |
| botToken              | string | EasyQQ验证密钥              |
| mailEnable            | bool   | 是否启用邮件功能（需要搭配EasyMail）  |
| mailAddress           | string | EasyMailAPI地址           |
| mailToken             | string | EasyMail验证密钥            |
| eventID               | string | CPP展演ID（一般是四位数字）        |
| enableTicketTypeCheck | bool   | 是否开启票种更新检测              |
| enableNoticeCheck     | bool   | 是否开启公告更新检测              |
