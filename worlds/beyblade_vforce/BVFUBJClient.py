from typing import Any

import worlds._polyemu as polyemu
import worlds._polyemu.context as polyctx
from .Constants import world_constants as WC

class BVFUBJClient(polyemu.PolyEmuClient):
    game = WC.GAME_NAME                    # must match your world's game name
    platform = polyemu.PLATFORMS.GBA       # one platform, or a tuple of platforms
    patch_suffix = ".apbvfubj"             # patch extension(s) this client opens, or None

    last_map_id: int
    ctx: "polyctx.PolyEmuClientContext"

    async def validate_rom(self, ctx) -> bool: ...


    async def game_watcher(self, ctx) -> None:
        if not await self.check_ingame():
            return

        # await self.lm_update_non_savable_ram()  Probably don't need this
        await self.beyblade_check_locations()
        await self.give_beyblade_items()

    async def on_package(self, ctx, cmd: str, args: dict[str, Any]) -> None:
        super().on_package(ctx, cmd, args) # required for UT's purposes

        match cmd:
            case "Connected":


    # Read the 14 collectible bytes
    def get_flag(flag_num: int):
        byte_index = flag_num // 8
        flag_idx = index % 8
        return bool(collectible_bytes[byte_idx] & (1 << flag_idx))