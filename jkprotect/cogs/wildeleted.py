import gd

gdcl=gd.Client()

class gmd:

	async def level(id):
		lvl=await gdcl.get_level(id)
	
		passw=f"Password: `{lvl.password}`" if lvl.is_copyable()==True else "Password: `Not copyable`"
		rating=''
		resp=f'''
		<b>
		Level name: `{lvl.name}`
		Creator: `{lvl.creator}`
		Description: `{lvl.description}`
		Downloads: `{lvl.downloads}`
		Likes: `{lvl.rating}`


		{passw}

		</b>'''


print(gmd.slevel(1))