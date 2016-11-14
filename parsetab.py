
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'D433BAA3226169191406726082B06ED6'
    
_lr_action_items = {'DOWN':([2,],[10,]),'GO':([0,],[2,]),'TOP':([2,],[5,]),'RIGHT':([2,],[11,]),'LEFT':([2,],[7,]),'$end':([1,3,4,5,6,7,8,9,10,11,],[0,-5,-3,-8,-1,-6,-4,-2,-9,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'direction':([2,],[6,]),'right':([2,],[4,]),'down':([2,],[3,]),'move':([0,],[1,]),'top':([2,],[8,]),'left':([2,],[9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> move","S'",1,None,None,None),
  ('move -> GO direction','move',2,'p_move','main.py',63),
  ('direction -> left','direction',1,'p_direction','main.py',67),
  ('direction -> right','direction',1,'p_direction','main.py',68),
  ('direction -> top','direction',1,'p_direction','main.py',69),
  ('direction -> down','direction',1,'p_direction','main.py',70),
  ('left -> LEFT','left',1,'p_left','main.py',75),
  ('right -> RIGHT','right',1,'p_right','main.py',79),
  ('top -> TOP','top',1,'p_top','main.py',83),
  ('down -> DOWN','down',1,'p_down','main.py',87),
]
