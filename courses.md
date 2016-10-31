---
layout: page
title: Courses
---

#### Data Science-Related Courses at UC Berkeley

These are semester-long computational courses (in some academic domain) or data-intensive courses at UC Berkeley. If you have suggestions or things to add, please [email](mailto:marwahaha@berkeley.edu). 

Department: <select style="height: 25px" id="search-dept" name="dept">
  <option></option>
  <option>African American Studies (AFRICAM)</option>
  <option>American Studies (AMERSTD)</option>
  <option>Anthropology (ANTHRO)</option>
  <option>Architecture (ARCH)</option>
  <option>Asian American Studies Program (ASAMST)</option>
  <option>Bioengineering (BIO ENG)</option>
  <option>Civil and Environmental Engineering (CIV ENG)</option>
  <option>Cognitive Science (COG SCI)</option>
  <option>Computer Science (COMPSCI)</option>
  <option>Demography (DEMOG)</option>
  <option>Earth and Planetary Science (EPS)</option>
  <option>Economics (ECON)</option>
  <option>Electrical Engineering (EL ENG)</option>
  <option>Engineering (ENGIN)</option>
  <option>Environmental Design (ENV DES)</option>
  <option>Environmental Economics and Policy (ENVECON)</option>
  <option>Environmental Science, Policy, and Management (ESPM)</option>
  <option>Geography (GEOG)</option>
  <option>Industrial Engineering and Operations Research (IND ENG)</option>
  <option>Industrial Engineering and Operations Reserach (IEOR)</option>
  <option>Information (INFO)</option>
  <option>Interdisciplinary Studies Field Major (ISF)</option>
  <option>International and Area Studies (IAS)</option>
  <option>Linguistics (LINGUIS)</option>
  <option>Mass Communications (MASSCOM)</option>
  <option>Mathematics (MATH)</option>
  <option>Mechanical Engineering (MEC ENG)</option>
  <option>Media Studies (MEDIAST)</option>
  <option>Middle Eastern Studies (M E STU)</option>
  <option>Molecular and Cell Biology (MCELLBI)</option>
  <option>Native American Studies (NATAMST)</option>
  <option>Nuclear Engineering (NUC ENG)</option>
  <option>Nutritional Sciences and Toxicology (NUSCTX)</option>
  <option>Philosophy (PHILOS)</option>
  <option>Physics (PHYSICS)</option>
  <option>Psychology (PSYCH)</option>
  <option>Public Health (PB HLTH)</option>
  <option>School of Information (INFO)</option>
  <option>Sociology (SOCIOL)</option>
  <option>Statistics (STAT)</option>
  <option>Undergraduate Business Administration (UGBA)</option>
</select>

Course Cluster: <select style="margin-bottom: 10px; height: 25px" id="filter-clusters">
  <option></option>
  <option>Humanities</option>
  <option>Social Science</option>
  <option>Biological Science</option>
  <option>Engineering</option>
  <option>Computer Science</option>
  <option>Mathematics/Statistics</option>
  <option>Physical Science</option>
</select>

<table id="project-table" class="table table-bordered" style="padding:0px; width:100%">
  <thead>
    <th data-dynatable-column="name" style="width:40%">Course Name</th>
    <th data-dynatable-column="dept" style="width:30%">Department</th>
    <th data-dynatable-column="number" style="width:10%">#</th>
    <th data-dynatable-column="cluster" style="width:20%">Cluster(s)</th>
  </thead>
  {% for p in site.pages %}
    {% if p.layout == 'course' %}
      <tr>
        <td class="project-name" style="width:40%">
          <a target="_blank" href="/datamap{{ p.url }}">{{ p.course-name }}</a>
        </td>
        <td class="dept" style="width:30%">{{ p.department }}</td>
        <td class="courseno" style="width:10%">{{ p.course }}</td>
        <td class="cluster" style="width:20%">
          {% if p.cluster[1] %} 
            Multiple <span style="display:none"> {{ p.cluster}} </span> 
          {% else %}
           {{ p.cluster }} 
          {% endif %}
        </td>
      </tr>
    {% endif %}
  {% endfor %}
</table>



<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Dynatable/0.3.1/jquery.dynatable.min.js"></script>

<script>
$('#project-table').bind('dynatable:init', function(e, dynatable) {
    dynatable.queries.functions['filter-clusters'] = function(record, queryValue) {
      console.log(record);
      return record.cluster.indexOf(queryValue) > -1;
    };
  }).dynatable({
    inputs: {
      // paginationClass: 'pagination',
      // paginationActiveClass: 'active',
      // paginationDisabledClass: 'disabled'
      queries: $('#search-dept, #filter-clusters')
    },
    features: {
      paginate: false,
      recordCount: false,
      search: false
    }
});
</script>


<br />


### Other Useful Links:
* Data Science related [Course List, maintained by D-Lab](http://dlab.berkeley.edu/course-list){:target="_blank"}
* Data 8: [List of connector courses](http://databears.berkeley.edu/sp16){:target="_blank"}
* Khoa's [Data Science at Berkeley Guide](http://kqdtran.github.io/so-i-heard-youre-an-aspiring-golden-bear-data-scient-ish/)


### Ideas for Improvement:

* a course map of data science courses, analogous to efforts by [HKN](https://hkn.eecs.berkeley.edu/courseguides)
* a course guide with a brief summary of each data science course
* a decision tree ("if I'm interested in this and I've taken this class, what should I take next?")