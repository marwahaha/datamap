---
layout: page
title: Support
---

Relevant data science resource centers on campus.

<table id="partner-table" class="table table-bordered">
  <thead>
    <th>Name, description, link</th>
    <th>graduate vs undergraduate</th>
    <th>Social Science vs Numeric</th>
    <th>1:1 vs weekly vs lecture-style</th>
  </thead>
  {% for p in site.pages %}
    {% if p.layout == 'partner' %}
      <tr>
        <td class="partner-name">
          {% if p.is-full-page %}
            <a class="partner-name" href="{{ p.url }}">{{ p.partner-name }}</a>
          {% else %}
            <span class="partner-name">{{ p.partner-name }}</span>
          {% endif %}
          <br />
          {{ p.partner-description }}<br />
          <a href="{{ p.partner-url }}">{{ p.partner-url }}</a>
        </td>
        <td class="partner-contact">{{ p.partner-contact }}</td>
        <td class="partner-tags">{{ p.partner-tags }}</td>
        <td class="partner-tags">{{ p.partner-tags }}</td>
      </tr>
    {% endif %}
  {% endfor %}
</table>



<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.js"></script>

<script>
$('#partner-table').dynatable({
    inputs: {
      paginationClass: 'pagination',
      paginationActiveClass: 'active',
      paginationDisabledClass: 'disabled'
    },
    features: {
      paginate: false
    }
});
</script>