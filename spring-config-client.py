from spring_config import ClientConfigurationBuilder
from spring_config.client import SpringConfigClient

config = (
    ClientConfigurationBuilder()
    .app_name("client-config")
    .address("http://localhost:8888")
    .profile("dev")
    .authentication(("root", "s3cr3t"))
    .build()
)

c = SpringConfigClient(config)
c.get_config()

print(c.get_attribute("default.msg"))
print(c.get_attribute("user.msg"))
print(c.get_attribute("user.role"))
print(c.get_attribute("user.password"))
