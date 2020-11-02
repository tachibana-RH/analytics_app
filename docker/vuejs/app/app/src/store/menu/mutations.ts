import { MutationTree } from 'vuex';
import { MenuState, Menu } from '@/store/types';

const mutations: MutationTree<MenuState> = {
  set: (state, data: Menu[]) => {
    state.menus = data;
  },
  add: (state, data: Menu) => {
    state.menus.push(data);
  },
  remove: (state, id: string) => {
    state.menus = state.menus.filter((e: Menu) => e.id !== id);
  },
};

export default mutations;