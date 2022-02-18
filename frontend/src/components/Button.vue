<template>
	<button @click="onClick">{{ text }}</button>
</template>

<script>
export default {
	name: "Button",
	props: {
		text: String,
		onClick: Function,
	},
};
</script>

<style scoped>
button {
	font-size: 1.2rem;
	padding: 6px 12px;
	margin-bottom: 0;

	display: inline-block;
	text-decoration: none;
	text-align: center;
	white-space: nowrap;
	vertical-align: middle;
	-ms-touch-action: manipulation;
	touch-action: manipulation;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	background-image: none;
	border: 1px solid transparent;
}
</style>
