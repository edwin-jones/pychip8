from pychip8.operations.set_x_to_y import SetXToY
from pychip8.operations.set_x import SetX
from pychip8.operations.set_i import SetI
from pychip8.operations.random import Random
from pychip8.operations.save_registers_zero_to_x import SaveRegistersZeroToX
from pychip8.operations.load_registers_zero_to_x import LoadRegistersZeroToX
from pychip8.operations.save_x_as_bcd import SaveXAsBcd

from pychip8.operations.graphics.clear_display import ClearDisplay

from pychip8.operations.jumps.goto import Goto
from pychip8.operations.jumps.goto_plus import GotoPlus
from pychip8.operations.jumps.skip_if_equal import SkipIfEqual
from pychip8.operations.jumps.skip_if_not_equal import SkipIfNotEqual
from pychip8.operations.jumps.skip_if_x_y_equal import SkipIfXyEqual
from pychip8.operations.jumps.skip_if_x_y_not_equal import SkipIfXyNotEqual
from pychip8.operations.jumps.return_from_function import ReturnFromFunction
from pychip8.operations.jumps.call_function import CallFunction

from pychip8.operations.arithmetic.add_to_x import AddToX
from pychip8.operations.arithmetic.add_y_to_x import AddYToX
from pychip8.operations.arithmetic.take_y_from_x import TakeYFromX
from pychip8.operations.arithmetic.take_x_from_y import TakeXFromY
from pychip8.operations.arithmetic.add_x_to_i import AddXToI

from pychip8.operations.bitwise.shift_x_left import ShiftXLeft
from pychip8.operations.bitwise.shift_x_right import ShiftXRight
from pychip8.operations.bitwise.bitwise_and import BitwiseAnd
from pychip8.operations.bitwise.bitwise_or import BitwiseOr
from pychip8.operations.bitwise.bitwise_xor import BitwiseXor

from pychip8.operations.timers.set_x_to_delay_timer import SetXToDelayTimer
from pychip8.operations.timers.set_sound_timer import SetSoundTimer
from pychip8.operations.timers.set_delay_timer import SetDelayTimer

from pychip8.operations.input.skip_if_key_pressed import SkipIfKeyPressed
from pychip8.operations.input.skip_if_key_not_pressed import SkipIfKeyNotPressed
from pychip8.operations.input.wait_for_key_press import WaitForKeyPress
