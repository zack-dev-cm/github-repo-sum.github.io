---
layout: default
title: Projects
---

# Projects

{% for project in site.data.projects %}
- [{{ project.title }}]({{ project.url | relative_url }})
{% endfor %}
