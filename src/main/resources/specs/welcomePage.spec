@objects
	header		#header .middle-wrapper
		logo	img
		caption	h1
	menu		#menu .middle-wrapper
		item-*	li

= Header =
	header:
		@on mobile
			height ~69 px
			centered horizontally inside screen

		@on dekstop
			height ~109 px
			inside screen 0px left right

	header.logo:
		inside header 0 px left, 8 to 50 px top bottom
		width 48 px
		height 48 px

	header.caption:
		right-of header.logo ~22 px

		@on desktop
			text is "Sample Website for Galen Framework"

		@on mobile
			text is "Sample Website"

= Menu =
	menu:
		aligned vertically all header

		@on mobile
			below header 1 px

		@on desktop
			below header 1 px

	menu.item-*:
		width > 30 px
		height ~64 px

	menu.item-1:
		inside menu 0 px left top

	@on desktop
		@forEach [menu.item-*] as menuItem, next as nextMenuItem
			${menuItem}:
				left-of ${nextMenuItem} 0 px
				aligned horizontally all ${nextMenuItem}

	@on mobile
		@for [1,2] as i
			menu.item-${i}:
				above menu.item-${i + 2} 0 px
				aligned vertically all menu.item-${i + 2}
		@for [1,3] as i
			menu.item-${i}:
				left-of menu.item-${i + 1} 0 px
				aligned horizontally all menu.item-${i + 1}





