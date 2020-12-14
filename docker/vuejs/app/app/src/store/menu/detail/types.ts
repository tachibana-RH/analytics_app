export interface RootState {
  version: string;
}

export interface MenuState {
  menus: Menu[]
}

export interface Menu {
  id: string;
  data: object;
}

