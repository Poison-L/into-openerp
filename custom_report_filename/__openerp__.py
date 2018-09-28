# -*- coding: utf-8 -*-
 

{
    'name': 'custom_report_filename',
    'version': '1.0',
    'category': 'Base',
    'author': 'CCDOS',
    'website': 'http://www.intoerp.com',
    'description': """

自定义报表文件名.
使用方法 可 参见 Invoice 报表 的定义。

定义文件名是在attachment字段指定一个python表达式。
 Save as Attachment Prefix：
(object.state in ('open','paid')) and ('INV'+(object.number or '').replace('/','')+'.pdf')



此模块在 buke 和 joshua 的指点下得以完成

关键代码来自：
http://stackoverflow.com/questions/14434846/openerp-custom-report-filename

Code added by Raul Paz to set the default file_name like the attach_name
        The attach_name mach with the attachment expresion from your report_xml
        <report
            id="report_webkit.YourModule_report_id"
            model="YourModule.model"
            name="Your_report_name"
            file="YOUR_MODULE/report/YOUR_MAKO_FILE.mako"
            string="Your Text in the print button"
            auto="False"
            report_type="webkit"
            attachment="'Valid_filename_expresion"
            usage="default"
        />
        And
        to modify existing report sale_report.xml to manage the name:
        create in your module a file : sale_report.xml
        <?xml version="1.0" encoding="UTF-8"?>
        <openerp>
           <data>
              <record id="sale.report_sale_order" model="ir.actions.report.xml">
                  <field name="attachment">(object.name or 'Sale Order')</field>
          <field name="attachment_use" eval="True"/>
      </record>
          </data>
        </openerp>




	""",
    'depends': ['web'],
    'data': [
     
    ],
    'installable': True,
    'auto_install': False,
    'web_preload': True,
    'js': ['static/src/js/none.js'],    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
