from docxtpl import DocxTemplate


def generate_from_data(template_file: str, out_file: str, data_list: list):
    """
    :param template_file: 模板文件名
    :param out_file: 输出文件名
    :param data_list:数据列表
    :return:
    """
    tpl = DocxTemplate(template_file)
    context = {'infos':data_list}
    tpl.render(context=context)
    tpl.save(out_file)


