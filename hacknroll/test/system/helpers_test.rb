require "application_system_test_case"

class HelpersTest < ApplicationSystemTestCase
  setup do
    @helper = helpers(:one)
  end

  test "visiting the index" do
    visit helpers_url
    assert_selector "h1", text: "Helpers"
  end

  test "creating a Helper" do
    visit helpers_url
    click_on "New Helper"

    fill_in "Helper score", with: @helper.helper_score
    click_on "Create Helper"

    assert_text "Helper was successfully created"
    click_on "Back"
  end

  test "updating a Helper" do
    visit helpers_url
    click_on "Edit", match: :first

    fill_in "Helper score", with: @helper.helper_score
    click_on "Update Helper"

    assert_text "Helper was successfully updated"
    click_on "Back"
  end

  test "destroying a Helper" do
    visit helpers_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Helper was successfully destroyed"
  end
end
