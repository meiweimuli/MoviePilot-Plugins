from typing import Any, List, Dict, Tuple

from app.plugins import _PluginBase

from app.log import logger


class Cookie115(_PluginBase):
    # 插件名称
    plugin_name = "cookie115"
    # 插件描述
    plugin_desc = "使用Cookie登录115网盘以及获取已登录115网盘的Cookie。"
    # 插件图标
    plugin_icon = "Filerun_A.png"
    # 插件版本
    plugin_version = "1.0"
    # 插件作者
    plugin_author = "gczran"
    # 作者主页
    author_url = ""
    # 插件配置项ID前缀
    plugin_config_prefix = "cookie115_"
    # 加载顺序
    plugin_order = 17
    # 可使用的用户级别
    auth_level = 1

    def init_plugin(self, config: dict = None):

        # 配置
        if config:
            cookie = config.get("cookie")
            logger.info(f"保存cookie：{cookie} ...")

    def get_state(self) -> bool:
        """
        获取插件运行状态
        """
        pass

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        """
        注册插件远程命令
        [{
            "cmd": "/xx",
            "event": EventType.xx,
            "desc": "名称",
            "category": "分类，需要注册到Wechat时必须有分类",
            "data": {}
        }]
        """
        pass

    def get_api(self) -> List[Dict[str, Any]]:
        """
        注册插件API
        [{
            "path": "/xx",
            "endpoint": self.xxx,
            "methods": ["GET", "POST"],
            "summary": "API名称",
            "description": "API说明"
        }]
        """
        pass

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        """
        拼装插件配置页面，需要返回两块数据：1、页面配置；2、数据结构
        """
        return [
            {
                'component': 'VForm',
                'content': [
                    {
                        'component': 'VTextarea',
                        'props': {
                            'model': 'address',
                            'label': 'Cookie',
                            'rows': 3,
                            'placeholder': ''
                        }
                    }
                ]
            }
        ], {
            "cookie": "",
        }

    def get_page(self) -> List[dict]:
        """
        拼装插件详情页面，需要返回页面配置，同时附带数据
        插件详情页面使用Vuetify组件拼装，参考：https://vuetifyjs.com/
        """
        pass

    def stop_service(self):
        """
        停止插件
        """
        pass
