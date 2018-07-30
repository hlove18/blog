class GamesController < ApplicationController

	def pentris
		# No view
		redirect_back fallback_location: root_path
		# Run python game
		fork do
			system "python2 " + Rails.public_path.join("python", "pentris", "tetris_bonus.py").to_s
			exit
		end
	end

end
