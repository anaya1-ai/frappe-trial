{
  "branch": "feature/feature_app_featureitem",
  "commits": [
    {
      "message": "Create feature_app and add FeatureItem DocType with fields title, description, status",
      "files": [
        {
          "path": "feature_app/feature_app/doctype/featureitem/featureitem.json",
          "content": "----BEGIN FILE----\n{\n \"doctype\": \"DocType\",\n \"name\": \"FeatureItem\",\n \"module\": \"feature_app\",\n \"custom\": 0,\n \"fields\": [\n  {\n   \"fieldname\": \"title\",\n   \"fieldtype\": \"Data\",\n   \"label\": \"Title\",\n   \"reqd\": 1\n  },\n  {\n   \"fieldname\": \"description\",\n   \"fieldtype\": \"Text\",\n   \"label\": \"Description\"\n  },\n  {\n   \"fieldname\": \"status\",\n   \"fieldtype\": \"Select\",\n   \"label\": \"Status\",\n   \"options\": \"Open\\nIn Progress\\nClosed\",\n   \"default\": \"Open\"\n  }\n ],\n \"permissions\": [\n  {\n   \"role\": \"System Manager\",\n   \"read\": 1,\n   \"write\": 1,\n   \"create\": 1,\n   \"delete\": 1\n  }\n ],\n \"istable\": 0,\n \"autoname\": \"field:title\",\n \"is_submittable\": 0\n}\n----END FILE----"
        },
        {
          "path": "feature_app/feature_app/__init__.py",
          "content": "----BEGIN FILE----\n# Init for feature_app\n----END FILE----"
        },
        {
          "path": "feature_app/feature_app/config/desktop.py",
          "content": "----BEGIN FILE----\n# Config for desktop icons etc\n----END FILE----"
        },
        {
          "path": "feature_app/hooks.py",
          "content": "----BEGIN FILE----\n# Hooks for feature_app\n\n# Automatically set status to Open on new FeatureItem\n\n# Instead of server script, use hooks event\n\ndoc_events = {\n    \"FeatureItem\": {\n        \"before_insert\": \"feature_app.feature_app.doctype.featureitem.featureitem.set_status_open\"\n    }\n}\n----END FILE----"
        },
        {
          "path": "feature_app/feature_app/doctype/featureitem/featureitem.py",
          "content": "----BEGIN FILE----\nimport frappe\n\ndef set_status_open(doc, method):\n    if not doc.status:\n        doc.status = \"Open\"\n----END FILE----"
        },
        {
          "path": "feature_app/setup.py",
          "content": "----BEGIN FILE----\n# Setup file for feature_app\nfrom setuptools import setup, find_packages\n\nwith open('README.md', 'r') as f:\n    long_description = f.read()\n\nsetup(\n    name='feature_app',\n    version='0.1',\n    description='Feature management app',\n    long_description=long_description,\n    author='Your Name',\n    packages=find_packages(),\n    zip_safe=False\n)\n----END FILE----"
        },
        {
          "path": "feature_app/README.md",
          "content": "----BEGIN FILE----\n# feature_app\n\nApp to manage feature items with status\n----END FILE----"
        }
      ]
    }
  ]
}