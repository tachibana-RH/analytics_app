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

export interface AnalyState {
  analy: Analy[]
}

export interface Analy {
  id: string;
  data: object;
}