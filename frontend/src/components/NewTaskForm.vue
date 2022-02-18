<template>
	<!-- TODO: Style this (with bootstrap) to make it look actually decent. -->
	<form>
		<input placeholder="Task Name" v-model="taskName" />
		<input placeholder="Task Description" v-model="taskDesc" />
	</form>
	<Button text="Create Task" @click="createTask(taskName, taskDesc)" />
</template>

<script>
import Button from "./Button.vue";
export default {
	name: "NewTaskForm",
	components: {
		Button,
	},
	data() {
		return {
			taskName: "",
			taskDesc: "",
		};
	},
	methods: {
		createTask(name, desc) {
			let newTask = {
				name: name,
				desc: desc,
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
