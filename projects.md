---
layout: page
title: Projects
---

### Groups doing Data Science Projects (and looking for help!)

Here is a list of research projects and consulting organizations that revolve around data science. If you have suggestions or things to add, please [email](mailto:marwahaha@berkeley.edu).

Education Level: <select id="search-edulevel" name="edulevel">
  <option></option>
  <option>Undergraduate</option>
  <option>Graduate</option>
</select>
<br />
Client Focus: <select id="search-client" name="client">
  <option></option>
  <option>Industry</option>
  <option>Research</option>
  <option>Development</option>
</select>
<br />
<table id="project-table" class="table table-bordered" style="padding:0px; width:100%">
  <thead>
    <th data-dynatable-column="name" style="width:50%">Project Group</th>
    <th data-dynatable-column="edulevel" style="width:20%">Education Level</th>
    <th data-dynatable-column="client">Client Focus</th>
  </thead>
  {% for p in site.pages %}
    {% if p.layout == 'project' %}
      <tr>
        <td class="project-name">
          <a target="_blank" href="/datamap{{ p.url }}">{{ p.project-name }}</a>
        </td>
        <td class="project-education-level">{{ p.project-education-level }}</td>
        <td class="project-academic-focus">{{ p.project-client-focus }}</td>
      </tr>
    {% endif %}
  {% endfor %}
</table>



<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.js"></script>

<script>
$('#project-table').bind('dynatable:init', function(e, dynatable) {
    dynatable.queries.functions['max-price'] = function(record, queryValue) {
      return parseFloat(record.price.replace(/,/,'')) <= parseFloat(queryValue);
    };
  }).dynatable({
    inputs: {
      // paginationClass: 'pagination',
      // paginationActiveClass: 'active',
      // paginationDisabledClass: 'disabled'
      queries: $('#search-edulevel, #search-client')
    },
    features: {
      paginate: false,
      recordCount: false,
      search: false
    }
});
</script>


<br />


### Ideas for Improvement:

* a list of data science projects on campus looking for interested students
* a matching platform for students and projects (could be via surveys)

If you have suggestions or things to add, please [email](mailto:marwahaha@berkeley.edu).


