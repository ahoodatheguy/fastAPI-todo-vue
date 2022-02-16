<template>
	<div class="task-container">
		<Task
			taskName="Task One"
			taskDesc="Lorem ipsum dolor sit amet, consectetur adipisicing elit."
		/>
	</div>
</template>

<script>
import Task from "./Task.vue";
export default {
	name: "Tasks",
	components: { Task },
};
</script>

<style scoped>
.task-container {
	text-align: start;
}
</style>
