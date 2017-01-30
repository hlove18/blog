# == Schema Information
#
# Table name: posts
#
#  id                     :integer          not null, primary key
#  title                  :string
#  body                   :text
#  description            :text
#  slug                   :string
#  created_at             :datetime         not null
#  updated_at             :datetime         not null
#  image_file_name        :string
#  image_content_type     :string
#  image_file_size        :integer
#  image_updated_at       :datetime
#  thumbnail_file_name    :string
#  thumbnail_content_type :string
#  thumbnail_file_size    :integer
#  thumbnail_updated_at   :datetime
#  published              :boolean          default("f")
#  published_at           :datetime
#

class Post < ApplicationRecord

	extend FriendlyId
 	friendly_id :title, use: :slugged

 	scope :published, -> { where(published: true) }

 	def should_generate_new_friendly_id?
 		title_changed?
 	end

 	def publish
 		update(published: true, published_at: Time.now)
 	end

 	def unpublish
 		update(published: false, published_at: nil)
 	end

 	#banner
 	has_attached_file :image, styles: { large: "825x200>", small: "100x100>" }, default_url: "/images/:style/missing.png"
  	validates_attachment_content_type :image, content_type: /\Aimage\/.*\z/

  	#thumbnail
  	has_attached_file :thumbnail, styles: { large: "100x100>", small: "50x50>" }, default_url: "/images/:style/missing.png"
  	validates_attachment_content_type :thumbnail, content_type: /\Aimage\/.*\z/
end
