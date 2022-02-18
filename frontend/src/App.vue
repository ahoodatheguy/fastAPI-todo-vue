<template>
	<div id="app">
		<Header text="FastAPI TODO App" />
		<div id="new-task">
			<Button v-if="showNew" text="New Task" @click="showNew = !showNew" />
			<NewTaskForm v-else />
		</div>
		<Tasks />
	</div>
</template>

<script>
import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
import Button from "./components/Button.vue";
import NewTaskForm from "./components/NewTaskForm.vue";

export default {
	name: "App",
	components: {
		Header,
		Tasks,
		Button,
		NewTaskForm,
	},
	data() {
		return { showNew: true };
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
