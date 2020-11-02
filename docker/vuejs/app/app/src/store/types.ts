export interface RootState {
  version: string;
}

export interface TodosState {
  todos: Todo[];
}

export interface Todo {
  // 一意になるかんじのID
  id: string;
  // チェックボックスON/OFF
  done: boolean;
  // やること
  text: string;
}

export interface MenuState {
  menus: Menu[]
}

export interface Menu {
  id: string;
  data: object;
}