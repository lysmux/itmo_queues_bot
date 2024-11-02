from .dialogs import routers as dialog_routers
from .handlers import routers as handler_routers

routers = (*handler_routers, *dialog_routers)
