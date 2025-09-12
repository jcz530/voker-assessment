<script lang="ts">
	import Button from '$lib/components/ui/button/button.svelte';
	import Label from '../ui/label/label.svelte';
	import Textarea from '../ui/textarea/textarea.svelte';
	import { Card, CardContent } from '../ui/card';
	import { useSubmitOrder } from '$lib/composables/useQueries';

	let message = '';
	let errorMessage = '';

	const submitOrder = useSubmitOrder();

	function handleSubmit(event: Event) {
		event.preventDefault();
		if (message.trim()) {
			errorMessage = '';
			$submitOrder.mutate(message, {
				onSuccess: () => (message = ''),
				onError: (error) => {
					errorMessage =
						error instanceof Error
							? error.message
							: 'An error occurred while submitting your order';
					console.error('Error submitting order:', error);
				}
			});
		}
	}

	function handleInput() {
		if (errorMessage) {
			errorMessage = '';
		}
	}
</script>

<div class="max-w-2xl mx-auto py-12">
	<h1 class="text-3xl font-bold text-primary-500 text-center">
		Welcome to <span class="bg-primary-500 px-2 text-4xl text-white inline-block skew-x-12"
			>VokerBurger</span
		>
	</h1>
	<h2
		class="text-2xl text-center bg-gradient-to-br from-primary-400 to-primary-500 mt-4 text-primary-50"
	>
		Home of the VokerBurger
	</h2>

	<form onsubmit={handleSubmit} class=" mt-16">
		<Label for="order-input" class="block text-xl text-slate-600 font-medium">
			What would you like to order?
		</Label>
		<div class="relative overflow-hidden p-2">
			<Textarea
				id="order-input"
				bind:value={message}
				oninput={handleInput}
				disabled={$submitOrder.isPending}
				placeholder="Enter your fast food order here... (e.g., 2 VokerBurgers, 2 fries, 1 Coke)"
				class="w-full min-h-[200px] p-4 mt-2 disabled: animate-pulse "
			/>
			{#if $submitOrder.isPending}
				<div
					class="bg-primary-100 h-1/2 w-full rounded-full absolute top-1/3 slow-animation animate-ping duration-3000"
				></div>
			{/if}
		</div>

		{#if errorMessage}
			<Card class="mt-4 border-red-500 bg-red-100 mx-2 ">
				<CardContent class="p-4">
					<p class="text-red-700 text-sm">{errorMessage}</p>
				</CardContent>
			</Card>
		{/if}

		<Button
			type="submit"
			disabled={!message.trim() || $submitOrder.isPending}
			class="w-full mt-12"
			size="lg"
			variant="default"
		>
			{$submitOrder.isPending ? 'Submitting...' : 'Submit Order'}
		</Button>
	</form>
</div>

<style>
	.slow-animation {
		animation-duration: 1.5s;
		opacity: 40%;
	}
</style>
