<script lang="ts">
	import type { ItemType } from '$lib/types';
	import { Beef, CupSoda, Leaf } from 'lucide-svelte';
	import { useOrders } from '$lib/composables/useQueries';
	import { itemLabels } from '$lib/composables/useOrderString';

	interface Props {
		itemType: ItemType;
	}

	let { itemType }: Props = $props();

	const ordersQuery = useOrders();

	const amount = $derived(() => {
		if (!$ordersQuery.data) return 0;

		return $ordersQuery.data
			.filter((order) => !order.canceled_at)
			.reduce((total, order) => {
				const itemCount = order.items
					.filter((item) => item.type === itemType)
					.reduce((sum, item) => sum + item.amount, 0);
				return total + itemCount;
			}, 0);
	});

	function getColor(type: ItemType) {
		switch (type) {
			case 'burger':
				return 'from-primary-300 to-primary-500 border-red-200';
			case 'drink':
				return 'from-blue-300 to-blue-500 border-blue-200';
			case 'fries':
				return 'from-yellow-300 to-yellow-500 border-yellow-200';
		}
	}

	function getIconColor(type: ItemType) {
		switch (type) {
			case 'burger':
				return 'text-red-600';
			case 'drink':
				return 'text-blue-600';
			case 'fries':
				return 'text-yellow-600';
		}
	}
</script>

<div class={`relative overflow-hidden rounded-xl  p-6`}>
	<div class="flex items-center justify-between">
		<div class="flex items-center gap-3">
			<div class={`rounded-full p-2 bg-white/40 ${getIconColor(itemType)}`}>
				{#if itemType === 'burger'}
					<Beef size={24} />
				{:else if itemType === 'drink'}
					<CupSoda size={24} />
				{:else if itemType === 'fries'}
					<Leaf size={24} />
				{/if}
			</div>
			<div>
				<h3 class="text-lg font-medium text-slate-700 capitalize">
					{itemLabels[itemType].plural}
				</h3>
			</div>
		</div>
		<div class="text-right">
			<div
				class={`text-3xl font-bold transition-colors ${amount() === 0 ? 'text-slate-400' : 'text-slate-00'}`}
			>
				{$ordersQuery.isPending ? '' : amount()}
			</div>
		</div>
	</div>
	<div class={`w-full block h-1 rounded-full mt-4 bg-gradient-to-br ${getColor(itemType)}`}></div>
</div>
