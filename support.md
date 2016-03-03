---
layout: page
title: Support
---

### Data Science Support Systems at UC Berkeley

Here is a list of different resources available to researchers and students. If you have suggestions or things to add, please [email](mailto:marwahaha@berkeley.edu).

Education Level: <select id="search-edulevel" name="edulevel">
  <option></option>
  <option>Undergraduate</option>
  <option>Graduate</option>
</select>
<br />
Academic Focus: <select id="search-academic" name="academic">
  <option></option>
  <option>Natural Science</option>
  <option>Social Science</option>
</select>
<br />
Teaching Style: <select id="search-style" name="style">
  <option></option>
  <option>1 on 1 Consulting</option>
  <option>Weekly Meetings</option>
  <option>Workshops</option>
</select>
<br />
<table id="partner-table" class="table table-bordered" style="padding:0px; width:100%">
  <thead>
    <th data-dynatable-column="name" style="width:40%">Resource</th>
    <th data-dynatable-column="academic" style="width:22%">Academic Focus</th>
    <th data-dynatable-column="edulevel" style="width:20%">Education Level</th>
    <th data-dynatable-column="style">Teaching Style</th>
  </thead>
  {% for p in site.pages %}
    {% if p.layout == 'partner' %}
      <tr>
        <td class="resource-name">
          <a target="_blank" href="/datamap{{ p.url }}">{{ p.resource-name }}</a>
        </td>
        <td class="resource-academic-focus">{{ p.resource-academic-focus }}</td>
        <td class="resource-education-level">{{ p.resource-education-level }}</td>
        <td class="resource-teaching-style">{{ p.resource-teaching-style }}</td>
      </tr>
    {% endif %}
  {% endfor %}
</table>



<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.js"></script>

<script>
$('#partner-table').bind('dynatable:init', function(e, dynatable) {
    dynatable.queries.functions['max-price'] = function(record, queryValue) {
      return parseFloat(record.price.replace(/,/,'')) <= parseFloat(queryValue);
    };
  }).dynatable({
    inputs: {
      // paginationClass: 'pagination',
      // paginationActiveClass: 'active',
      // paginationDisabledClass: 'disabled'
      queries: $('#search-edulevel, #search-academic, #search-style')
    },
    features: {
      paginate: false,
      recordCount: false,
      search: false
    }
});
</script>