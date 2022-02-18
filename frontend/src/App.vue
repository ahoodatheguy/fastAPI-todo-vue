<template>
	<div id="app">
		<Header text="FastAPI TODO App" />
		<Button text="New Task" :onClick="createTask" />
		<Tasks />
	</div>
</template>

<script>
import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
import Button from "./components/Button.vue";

export default {
	name: "App",
	components: {
		Header,
		Tasks,
		Button,
	},
	methods: {
		createTask() {
			// TODO: Create a component that handles user input, instead of using prompt();
			let newTask = {
				name: prompt("Task name"),
				desc: prompt("Task Description"),
			};
			fetch("http://localhost:8000/create-task", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(newTask),
			});
			// TODO: Access fetchTasks() from the Tasks component and use it here to avoid reloads.
			location.reload();
		},
	},
};
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
	padding-left: 2rem;
	padding-right: 2rem;
}
</style>
