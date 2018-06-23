class AddIndexToPosts < ActiveRecord::Migration[5.0]
  def change
  	add_index(:posts, :published)
	add_index(:posts, :published_at)
  end
end
