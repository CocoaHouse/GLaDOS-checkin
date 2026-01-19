在（Settings → Secrets and variables → Actions → New repository secret）中添加两个变量：

GLADOS_AUTH 填用户的Authoration（目前已不需要）

GLADOS_COOKIE 填自己的Cookie（在签到页面查看Request Headers里面的Cookie项）

修改后在（Actions → 左侧Glados Daily Checkin ->右侧runworkflow）执行测试后刷新一下，点进去看测试结果，检查Run Checkin Script部分的返回值看是否执行成功
