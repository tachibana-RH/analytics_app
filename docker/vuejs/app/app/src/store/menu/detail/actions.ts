// import { ActionTree } from 'vuex';
// import { MenuState, RootState, Menu } from '@/store/types';
// import { ApiRqsV1 } from '../../../methods/ApiRequestV1'

// const actions: ActionTree<MenuState, RootState> = {
//   set: ({ commit }, data: Menu[]) => {
//     commit('set', data);
//     return true;
//   },

//   add: async ({ commit }, analy: Menu) => {
//     await ApiRqsV1('POST', '/menu/new', analy, false)
//     .catch(err => {
//       // 失敗
//       console.error(err);
//       return false;
//     });
//     // 成功
//     commit('add', analy);
//     return true;
//   },

//   remove: async ({ commit }, id: string) => {
//     await ApiRqsV1('DELETE', '/menu/delete', {id: id}, false)
//     .catch(err => {
//       console.error(err);
//       return false;
//     });
//     commit('remove', id);
//     return true;
//   },

// };

// export default actions;