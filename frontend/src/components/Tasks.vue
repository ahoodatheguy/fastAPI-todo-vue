<template>
	<div class="task-container">
		<div v-for="task in tasks" :key="task.id">
			<Task :taskName="task.name" :taskDesc="task.desc" :taskID="task.id" />
		</div>
	</div>
</template>

<script>
import Task from "./Task.vue";
export default {
	name: "Tasks",
	components: { Task },
	data() {
		return {
			tasks: {},
		};
	},
	methods: {
		fetchTasks() {
			fetch("http://localhost:8000/")
				.then((response) => response.json())
				.then((data) => (this.tasks = data));
		},
	},
	created() {
		this.fetchTasks();
	},
};
</script>

<style scoped>
.task-container {
	text-align: start;
}
</style>
