<template>
	<div class="task-container">
		<h3 class="task-name" @click="deleteTask(taskID)">{{ taskName }}</h3>
		<p class="task-details">
			{{ taskDesc }}
		</p>
	</div>
</template>

<script>
export default {
	name: "Task",
	props: {
		taskName: String,
		taskDesc: String,
		taskID: Number,
	},
	methods: {
		deleteTask(id) {
			// TODO: Add a dialog box component with VUE to make user confirm.
			if (confirm("Really delete task? ")) {
				fetch(`http://localhost:8000/delete/${id}`, { method: "DELETE" });
				// TODO: After deletion, call the fetchTasks() (emits?) function from Tasks.vue (the parent) to avoid having to reload page.
				location.reload();
			}
		},
	},
};
</script>

<style scoped>
.task-details {
	color: gray;
}
.task-name:hover {
	text-decoration: line-through;
	cursor: pointer;
}
</style>
