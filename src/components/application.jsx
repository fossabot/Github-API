import React from 'react';
import Freezer from 'freezer-js';
import querystringparser from 'querystringparser';
import reqwest from 'reqwest';

import ProjectList from 'components/projectlist';
import emptystate from 'emptystate';
import exampleProjects from 'exampleprojectsdata';

const freezer = new Freezer(emptystate);

var extension = "/projects"

var queryString = {}
if(window.location.search !== ""){
  queryString = querystringparser.parse(window.location.search.substr(1));
}

var projectsSetter = () => {
  freezer.get().set("projects", exampleProjects);
}

if(queryString["server"]){
  projectsSetter = () => {
    reqwest({
        url: queryString["server"] + extension
      , method: 'get'
      ,type: 'json'
      , success: resp => {
          console.log(resp)
          freezer.get().set("projects", resp)
        }
    })
  }
}
projectsSetter();

window.freezer = freezer;

export default class Application extends React.Component{
  componentDidMount(){
    freezer.on('update', newvalue => this.forceUpdate());
  }
  render(){
    var originalOutput = () => {
	alert('Arranging in intial order');
	extension = "/projects";
	projectsSetter();
    }
    var max_minOutput = () => {
	alert('Arranging by open issues (max to min)');
	extension = "/filter_max_min";
	projectsSetter();
    }
    var min_maxOutput = () => {
	alert('Arranging by open issues (min to max)');
	extension = "/filter_min_max";
	projectsSetter();
    }
    var contributorsOutput = () => {
	alert('Arranging by the number of contributors');
	extension = "/filter_contributors";
	projectsSetter();
    }
	
    const state = freezer.get();
    return (<div className="container">
      <h1>{state.title}</h1>
      <p>Filtering options:</p>    
	<span>
		<div class="btn-group" role="group" aria-label="...">
  			<button onClick={originalOutput} type="button" class="btn btn-default">Initial state</button>
  			<button onClick={max_minOutput} type="button" class="btn btn-default">Max open issues first</button>
  			<button onClick={min_maxOutput} type="button" class="btn btn-default">Min open issues first</button>
			<button onClick={contributorsOutput} type="button" class="btn btn-default">Filtered by contributors number</button>
		</div>				
	</span>

      <ProjectList projects={state.projects}/>
    </div>);
  }
}

