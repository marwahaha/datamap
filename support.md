---
layout: page
title: Support
---

<table id="partner-table" class="table table-bordered" style="padding:0px">
  <thead>
    <th>Resource</th>
    <th>Education Level</th>
    <th>Academic Focus</th>
    <th>Teaching Style</th>
  </thead>
  {% for p in site.data.resources %}
    <tr>
      <td class="resource-name">
        <a target="_blank" href="{{ p.resource-url }}">{{ p.resource-name }}</a>
      </td>
      <td class="resource-education-level">{{ p.resource-education-level }}</td>
      <td class="resource-academic-focus">{{ p.resource-academic-focus }}</td>
      <td class="resource-teaching-style">{{ p.resource-teaching-style }}</td>
    </tr>
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