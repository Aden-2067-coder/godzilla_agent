def on_block_broken_of_netherite():
    agent.collect_all()
blocks.on_block_broken(BLOCK_OF_NETHERITE, on_block_broken_of_netherite)

def on_on_chat():
    player.tell(mobs.target(NEAREST_PLAYER), "Hi!")
player.on_chat("\"hello. im your Agent\"", on_on_chat)

mobs.spawn(AGENT, pos(200, 64, 64))
gameplay.set_difficulty(NORMAL)
agent.set_slot(1)
agent.teleport_to_player()
agent.move(FORWARD, 2)
agent.move(BACK, 2)
agent.move(LEFT, 2)
agent.move(RIGHT, 2)
agent.destroy(FORWARD)
agent.attack(FORWARD)
agent.collect(DIAMOND)
agent.detect(END_PORTAL)