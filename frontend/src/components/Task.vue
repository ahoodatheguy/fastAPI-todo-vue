<template>
	<div class="task-container">
		<h3 class="task-name">{{ taskName }}</h3>
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
	},
};
</script>

<style scoped>
.task-details {
	color: gray;
}
</style>
