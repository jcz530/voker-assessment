import type { Order } from '$lib/types';

export const itemLabels = {
	burger: { singular: 'burger', plural: 'burgers' },
	fries: { singular: 'fries', plural: 'fries' },
	drink: { singular: 'drink', plural: 'drinks' }
};

function pluralize(count: number, singular: string, plural: string): string {
	if (count === 1) {
		return `1 ${singular}`;
	}
	return `${count} ${plural}`;
}

function oxfordComma(parts: string[]): string {
	if (parts.length === 0) return '';
	if (parts.length === 1) return parts[0];
	if (parts.length === 2) return `${parts[0]} and ${parts[1]}`;

	const lastPart = parts[parts.length - 1];
	const otherParts = parts.slice(0, -1);
	return `${otherParts.join(', ')}, and ${lastPart}`;
}

export function useOrderString() {
	function getOrderString(order: Order): string {
		const itemCounts = order.items.reduce(
			(acc, item) => {
				acc[item.type] = (acc[item.type] || 0) + item.amount;
				return acc;
			},
			{} as Record<string, number>
		);

		const parts: string[] = [];

		for (const [type, count] of Object.entries(itemCounts)) {
			if (count > 0 && itemLabels[type as keyof typeof itemLabels]) {
				const labels = itemLabels[type as keyof typeof itemLabels];
				parts.push(pluralize(count, labels.singular, labels.plural));
			}
		}

		return oxfordComma(parts);
	}

	return { getOrderString };
}
