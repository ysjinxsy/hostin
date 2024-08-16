import aiosqlite #type: ignore
import asyncio
DATABASE_PATH = 'database.db'

async def update_database():
    guild_id = '1273388243626496033'  # Replace with your actual guild ID
    assistant_manager_role_id = '1273397337535807692'  # Replace with the desired role ID
    manager_role_id = '1273397318766563339'  # Replace with the desired role ID
    channel_id = '1273397560106680421'  # Replace with the desired channel ID
    roster = '20'  # Replace with the new roster value

    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.cursor() as cursor:
            # Update Assistant Manager Role
            await cursor.execute(
                "UPDATE config SET assistant_manager_role_id = ? WHERE guild_id = ?",
                (assistant_manager_role_id, guild_id)
            )
            # Update Manager Role
            await cursor.execute(
                "UPDATE config SET manager_role_id = ? WHERE guild_id = ?",
                (manager_role_id, guild_id)
            )
            # Update Channel ID
            await cursor.execute(
                "UPDATE config SET channel_id = ? WHERE guild_id = ?",
                (channel_id, guild_id)
            )
            # Update Roster
            await cursor.execute(
                "UPDATE config SET roster = ? WHERE guild_id = ?",
                (roster, guild_id)
            )
            await db.commit()
            print("Database updated successfully.")


if __name__ == "__main__":
    asyncio.run(update_database())
