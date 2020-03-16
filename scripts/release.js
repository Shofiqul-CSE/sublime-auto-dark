const execa = require('execa')
const fs = require('fs')
const inquirer = require('inquirer')
const semver = require('semver')

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

const release = async() => {
  const curVersion = JSON
    .parse(fs.readFileSync('./package.json', 'utf8'))
    .version

  console.log(`[./scripts/release.js] Current version: st4-${curVersion}`)

  const bumps = ['major', 'minor', 'patch', 'prerelease']
  const versions = {}
  bumps.forEach(b => {
    versions[b] = semver.inc(curVersion, b)
  })
  const bumpChoices = bumps.map(b => ({ name: `${b} (${versions[b]})`, value: b }))

  const { bump } = await inquirer.prompt([
    {
      name: 'bump',
      message: 'Select release type:',
      type: 'list',
      choices: [
        ...bumpChoices
      ]
    }
  ])

  const version = versions[bump]

  const { yes } = await inquirer.prompt([
    {
      name: 'yes',
      message: `Confirm releasing st4-${version}?`,
      type: 'list',
      choices: ['Cancel', 'Ok']
    }
  ])

  if (yes === 'Cancel') {
    console.log('[./scripts/release.js] cancelled.')
    return
  }

  await execa('npm', ['--no-git-tag-version', 'version', version], { stdio: 'inherit' })
  await execa('git', ['add', '-A'], { stdio: 'inherit' })
  await execa('git', ['commit', '-m', `bump: Bump package from st4-${curVersion} to st4-${version}`], { stdio: 'inherit' })

  // assuming conventional-changelog-cli is installed globally via npm or yarn
  await execa('conventional-changelog', ['-p', 'angular', '-i', 'CHANGELOG.md', '-s'], { stdio: 'inherit' })

  await execa('git', ['add', '-A'], { stdio: 'inherit' })
  await execa('git', ['commit', '-m', `docs(CHANGELOG): Update CHANGELOG to st4-${version}`], { stdio: 'inherit' })

  await execa('git', ['commit', '--allow-empty', '-S', '-m', `release: st4-${version}`], { stdio: 'inherit' })
  await execa('git', ['tag', '-s', `st4-${version}`, '-m', `st4-${version}`], { stdio: 'inherit' })
  await execa('git', ['push', 'origin', 'master', '--tags'], { stdio: 'inherit' })

  console.log(`[./scripts/release.js] Done releasing version: st4-${version}`)
}

release().catch(err => {
  console.error(err)
  process.exit(1)
})
