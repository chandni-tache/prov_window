''' Contains all the configurations for the application. '''

import constants


# Define our default configuration settings
CONFIG_OPTIONS = {
    "allow_external_content": {"default": False, "type": bool},
    "allow_plugins":          {"default": False, "type": bool},
    "allow_popups":           {"default": False, "type": bool},
    "allow_printing":         {"default": False, "type": bool},
    "bookmarks":              {"default": {}, "type": dict},
    "bookmarks_Combo":          {"default": {}, "type": dict},
    "content_handlers":       {"default": {}, "type": dict},
    "default_encoding":       {"default": "utf-8", "type": str},
    "default_password":       {"default": None, "type": str},
    "default_user":           {"default": None, "type": str},
    "enable_diagnostic":      {"default": False, "type": bool},
    "force_js_confirm":       {"default": "ask", "type": str,
                               "values": ("ask", "accept", "deny")},
    "fullscreen":             {"default": False, "type": bool},
    "icon_theme":             {"default": None, "type": str},
    "navigation":             {"default": True, "type": bool},
    "navigation_layout":      {"default":
                               ['back', 'forward', 'refresh', 'stop',
                                'zoom_in', 'zoom_out', 'separator',
                                'bookmarks', 'separator', 'spacer',
                                'quit','Bookmarks_Combo'], "type": list},
    "network_down_html":      {"default": constants.DEFAULT_NETWORK_DOWN,
                               "type": str, "is_file": True},
    "page_unavailable_html":  {"default": constants.DEFAULT_404, "type": str,
                               "is_file": True},
    "print_settings":         {"default": {}, "type": dict},
    "privacy_mode":           {"default": True, "type": bool},
    "proxy_server":           {"default": None, "type": str,
                               "env": "http_proxy"},
    "quit_button_mode":       {"default": "reset", "type": str,
                               "values": ["reset", "close"]},
    "quit_button_text":       {"default": "I'm &Finished", "type": str},
    "screensaver_url":        {"default": "about:blank", "type": str},
    "ssl_mode":               {"default": "strict", "type": str,
                               "values": ["strict", "ignore"]},
    "start_url":              {"default": "about:blank", "type": str},
    "stylesheet":             {"default": None, "type": str},
    "suppress_alerts":        {"default": False, "type": bool},
    "timeout":                {"default": 0, "type": int},
    "timeout_mode":           {"default": "reset", "type": str,
                               "values": ["reset", "close", "screensaver"]},
    "user_agent":             {"default": None, "type": str},
    "user_css":               {"default": None, "type": str},
    "whitelist":              {"default": None},  # don't check type here
    "window_size":            {"default": None},  # don't check type
    "zoom_factor":            {"default": 1.0, "type": float},
    "Restrictions":           {"default": {},  "type": dict},    
    "rule_id":                {"default": None,  "type": str},
    "rule_name":              {"default": None,  "type": str},
    "access_id":              {"default": 0,  "type": int}
}

# Base url for api
BASE_URL = "http://tachetechnologies.com/provApi/provConsole/api/v1/"
VIEW_RULE_URL = BASE_URL + "viewrulebylog"
INSERT_ACCESS_URL = BASE_URL + "insertAccessActivity"
