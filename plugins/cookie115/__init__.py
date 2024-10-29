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
