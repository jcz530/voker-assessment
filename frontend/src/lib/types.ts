export interface Item {
	amount: number;
	type: ItemType;
}

export enum ItemType {
	BURGER = 'burger',
	DRINK = 'drink',
	FRIES = 'fries'
}

export interface Order {
	canceled_at: Date;
	items: Item[];
	number: number;
}
