import os
import base64
import json

from jinja2 import Template, Environment, FileSystemLoader

SOURCE_DIR="./source"
DIST_DIR="./dist"

def get_icon_names(path: str):
    return list(map(lambda x : os.path.basename(x), os.listdir(path)))

def snake_to_pascal(snake_case_str):
    return ''.join(word.capitalize() for word in snake_case_str.split('_'))

def process(icon_name):
    rendering = render(icon_name)
    with open(f"dist/{snake_to_pascal(icon_name)}.puml", "w") as file:
        print(rendering , file=file)


def render(icon_name):
    env = Environment(loader=FileSystemLoader('./source/template/', encoding='utf8'))
    template = env.get_template("Entity.j2")
    parameters = {
        "pascal": snake_to_pascal(icon_name),
        "base64": png_to_base64(icon_name),
    }
    return template.render(parameters)

def main():
    icon_names = get_icon_names(f"{SOURCE_DIR}/icon/google-cloud-icons")
    icon_names.sort()
    for icon_name in icon_names:
        process(icon_name)

def img_to_base64(icon_name, ext):
    with open(f"{SOURCE_DIR}/icon/google-cloud-icons/{icon_name}/{icon_name}.{ext}", "rb") as file:
        data = base64.b64encode(file.read())
    return data.decode('utf-8')

def png_to_base64(icon_name):
    return img_to_base64(icon_name, "png")
def svg_to_base64(icon_name):
    return img_to_base64(icon_name, "svg")

def page_gen_service_icons():
    icon_names = get_icon_names(f"{SOURCE_DIR}/icon/google-cloud-icons")
    icon_names.sort()
    services = []
    
    for icon_name in icon_names:
        services.append({
            "snake": icon_name ,
            "pascal": snake_to_pascal(icon_name),
        })

    env = Environment(loader=FileSystemLoader('./source/template/', encoding='utf8'))
    template = env.get_template("ServiceIcons.j2")
    parameters = {"services": services}
    rendering = template.render(parameters)

    with open(f"example/service_icons.md", "w") as file:
        print(rendering , file=file)

def page_generate_gc_common():
    env = Environment(loader=FileSystemLoader('./source/template/', encoding='utf8'))
    template = env.get_template("GCCommon.j2")
    rendering = template.render()

    with open(f"dist/GCCommon.puml", "w") as file:
        print(rendering , file=file)

# process("bigquery")
page_gen_service_icons()
page_generate_gc_common()
main()