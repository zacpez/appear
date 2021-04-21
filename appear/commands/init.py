from appear.schema.namespaces import generate_schema


def generate_config(version, date):
    print(generate_schema(version, date))
