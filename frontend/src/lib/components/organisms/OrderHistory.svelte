<script lang="ts">
	import type { Order } from '$lib/types';
	import { ClipboardList, Package } from 'lucide-svelte';
	import { useOrders } from '$lib/composables/useQueries';
	import OrderHistoryRow from '$lib/components/atoms/OrderHistoryRow.svelte';

	const ordersQuery = useOrders();

	$: sortedOrders = $ordersQuery.data?.sort((a: Order, b: Order) => b.number - a.number) || [];
</script>

<div class="space-y-4">
	<div class="flex items-center gap-3">
		<ClipboardList size={24} class="text-primary-500" />
		<h2 class="text-2xl font-bold text-primary-500">Order History</h2>
	</div>

	{#if $ordersQuery.isPending}
		<div class="flex items-center justify-center py-12">
			<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-slate-600"></div>
			<span class="ml-3 text-slate-600">Loading orders...</span>
		</div>
	{:else if $ordersQuery.error}
		<div class="text-center py-12">
			<div class="text-red-600 font-medium">Error loading orders</div>
			<p class="text-slate-500 mt-1">{$ordersQuery.error.message}</p>
		</div>
	{:else if sortedOrders.length === 0}
		<div class="text-center py-16">
			<Package size={64} class="mx-auto text-primary-300 mb-4" />
			<h3 class="text-xl font-medium text-slate-600 mb-2">No orders yet</h3>
			<p class="text-slate-500">Orders will appear here once you start placing them.</p>
		</div>
	{:else}
		<div class="bg-primary-50 rounded-lg border border-primary-200 overflow-hidden">
			<div
				class="grid grid-cols-3 gap-4 p-4 bg-primary-200 border-b border-slate-200 font-bold text-sm text-primary-600"
			>
				<div>Order #</div>
				<div>Items</div>
				<div>Status</div>
			</div>
			{#each sortedOrders as order (order.number)}
				<OrderHistoryRow {order} />
			{/each}
		</div>
	{/if}
</div>
