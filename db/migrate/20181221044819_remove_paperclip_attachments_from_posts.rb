class RemovePaperclipAttachmentsFromPosts < ActiveRecord::Migration[5.2]
   	def up
   		remove_column :posts, :image_file_name
   		remove_column :posts, :image_content_type
   		remove_column :posts, :image_file_size
   		remove_column :posts, :image_updated_at
   		remove_column :posts, :thumbnail_file_name
   		remove_column :posts, :thumbnail_content_type
   		remove_column :posts, :thumbnail_file_size
   		remove_column :posts, :thumbnail_updated_at
	end

  	def down
    	add_column :posts, :image_file_name, :string
   		add_column :posts, :image_content_type, :string
   		add_column :posts, :image_file_size, :integer
   		add_column :posts, :image_updated_at, :datetime
   		add_column :posts, :thumbnail_file_name, :string
   		add_column :posts, :thumbnail_content_type, :string
   		add_column :posts, :thumbnail_file_size, :integer
   		add_column :posts, :thumbnail_updated_at, :datetime
  	end
end
