<template>
	<div class="header-container">
		<img class="header-logo" alt="Vue logo" src="../assets/logo.png" />
		<h2 class="title">{{ text }}</h2>
	</div>
</template>

<script>
export default {
	name: "Header",
	props: {
		text: String,
	},
};
</script>

<style scoped>
.header {
	margin: 2rem;
	display: flex;
	justify-content: space-evenly;
	flex-wrap: nowrap;
}
.header-logo {
	width: 7rem;
	height: 7rem;
}
.title {
}
</style>
