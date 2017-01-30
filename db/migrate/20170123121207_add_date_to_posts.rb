class AddDateToPosts < ActiveRecord::Migration[5.0]
  def change
    add_column :posts, :date, :string
  end
end
